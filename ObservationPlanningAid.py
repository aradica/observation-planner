import requests
from bs4 import BeautifulSoup


class ObservationPlanningAid:
    criteria_url = "https://cgi.minorplanetcenter.net/cgi-bin/neaobs_getlist.cgi"
    ephemeris_url = "https://cgi.minorplanetcenter.net/cgi-bin/mpeph.cgi"

    def __init__(self):
        pass

    def produce_object_list(self, criteria):
        r = requests.post(self.criteria_url, data={
            "date": 20190720,
            "ralo": -120,
            "rahi": +120,
            "declo": -90,
            "dechi": +90,
            "magbr": None,
            "magfa": 21.0,
            "motlo": 0.0,
            "mothi": 5.0,
            "mtype": "d",
            "elolo": 60,
            "elohi": 180,
            "gallat": 0,
            "unclo": 10,
            "unchi": 1800,
            "uncsig": 1,
            "dayssince": 0,
            "typ1": "V",
            "typ2": "P",
            "typ3": "t",
            "typ4": "p",
            "typ5": "m",
            "stat1": "N",
            "stat2": "M",
            "stat3": "1",
            "stat4": "P",
            "bel": 100,
            "bmag": 21.0,
            "sort": 1,
            "dirsort": 1,
            "oc": None,
            "ndate": None,
            "ephint": 1,
            "ephunit": "h",
            "raty": "a",
            "motty": "t",
            "motun": "m"
        })

        soup = BeautifulSoup(r.text, "html.parser")
        lines = str(soup.body.form.pre)[6:].splitlines()[:-1]
        names = []
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
    obs = ObservationPlanningAid()
    names = obs.produce_object_list("CRITERIA")
    print("OBJECTS:", names)
    obs.get_ephemeris(names)
