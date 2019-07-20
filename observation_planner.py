import requests
from bs4 import BeautifulSoup
from criteria import *


class ObservationPlanner:
    criteria_url = "https://cgi.minorplanetcenter.net/cgi-bin/neaobs_getlist.cgi"
    ephemeris_url = "https://cgi.minorplanetcenter.net/cgi-bin/mpeph.cgi"

    def __init__(self):
        pass

    def produce_object_list(self, criteria):
        r = requests.post(self.criteria_url, data={
            # Planned date of obs.
            "date": str(criteria.observingDate.date()).replace("-", ""),

            # Observability options
            "ralo": criteria.observability.RA_range[0],
            "rahi": criteria.observability.RA_range[1],
            "declo": criteria.observability.decl_range[0],
            "dechi": criteria.observability.decl_range[1],
            "magbr": criteria.observability.magnitude_range[0],
            "magfa": criteria.observability.magnitude_range[1],
            "motlo": criteria.observability.motion_range[0],
            "mothi": criteria.observability.motion_range[1],
            "mtype": criteria.observability.motion_unit,
            "elolo": criteria.observability.solar_elong[0],
            "elohi": criteria.observability.solar_elong[1],
            "gallat": criteria.observability.lower_galactic_lat_limit,

            # Uncertainty
            "unclo": criteria.uncertainty.current_uncertainty[0],
            "unchi": criteria.uncertainty.current_uncertainty[1],
            "uncsig": criteria.uncertainty.consider_sigma,
            "dayssince": criteria.uncertainty.days_since,

            # Object type
            "typ1": "V" if criteria.objectType.VIs else None,
            "typ2": "P" if criteria.objectType.PHAs else None,  # if
            "typ3": "t" if criteria.objectType.atens else None,  # ...
            "typ4": "p" if criteria.objectType.appolos else None,
            "typ5": "m" if criteria.objectType.amors else None,

            # Object status
            "stat1": "N" if criteria.objectStatus.numbered else None,
            "stat2": "M" if criteria.objectStatus.multiple_opposition_unnumbered else None,
            "stat3": "1" if criteria.objectStatus.current_opposition_one_opp_unnumbered else None,
            "stat4": "P" if criteria.objectStatus.previous_opposition_one_opp_unnumbered else None,
            "bel": criteria.objectStatus.ignore_brightening_at_solar_elongs_greater_than,
            "bmag": criteria.objectStatus.ignore_currently_brighter_than,
            # Display labels?

            # Result sorting
            "sort": {"designation": 1, "uncertainty": 2, "decl": 3, "ra": 4}.get(criteria.resultSorting.sort_by),
            "dirsort": {"increasing": 1, "decreasing": 2}.get(criteria.resultSorting.order),

            # MPES
            "oc": criteria.mpes.observatory_code,
            "ndate": criteria.mpes.n_of_ephemeris_dates,
            "ephint": criteria.mpes.ephemeris_interval,
            "ephunit": criteria.mpes.ephemeris_units,
            "raty": "a",
            "motty": "t",
            "motun": "m"
        })

        soup = BeautifulSoup(r.text, "html.parser")
        names = []

        # If there are objects with that criteria at that time
        if "pre" in dir(soup):
            lines = str(soup.body.form.pre)[6:].splitlines()[:-1]

            for line in lines:
                names.append(line.split("value=")[1][1:8])
        return names

    def get_ephemeris(self, object_list):
        r = requests.post(self.ephemeris_url, data={
            "Obj": object_list,
            "d": "2019 07 20",
            "l": 20,
            "i": 1,
            "u": "h",
            "c": None,
            "raty": "a",
            "s": "t",
            "m": "m",
            "nsig": 1
        })
        soup = BeautifulSoup(r.text, "html.parser")
        print(soup)
        # print(str(soup.body.pre)[6:-6])


if __name__ == "__main__":
    observingDate = ObservingDate(2019, 7, 20)
    observability = Observability(
        (-120, 120), (-90, 90), (0, 21), (0, 5), "d", (60, 180), 0)
    uncertainty = Uncertainty((10, 1800), 1, 0)
    objectType = ObjectType(1, 1, 1, 1, 1)
    objectStatus = ObjectStatus(1, 1, 1, 1, 100, 21, 1)
    resultSorting = ResultSorting(1, 1)
    mpes = MPES("L01", None, 1, "h", "a", "t", "m")

    criteria = Criteria(observingDate, observability, uncertainty, objectType,
                        objectStatus, resultSorting, mpes)

    obs = ObservationPlanner()
    names = obs.produce_object_list(criteria)
    print("OBJECTS:", names)
    obs.get_ephemeris(names)
