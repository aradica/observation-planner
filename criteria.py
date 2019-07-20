import datetime
from dataclasses import dataclass


class ObservingDate(datetime.datetime):
    """Data abstraction layer"""
    pass


@dataclass
class Observability:
    """Data abstraction layer"""
    RA_range: tuple
    decl_range: tuple
    magnitude_range: tuple
    motion_range: tuple
    motion_unit: str
    solar_elong: tuple
    lower_galactic_lat_limit: int


@dataclass
class Uncertainty:
    """Data abstraction layer"""
    current_uncertainty: tuple
    consider_sigma: int
    days_since: int


@dataclass
class ObjectType:
    """Data abstraction layer"""
    VIs: bool
    PHAs: bool
    atens: bool
    appolos: bool
    amors: bool


@dataclass
class ObjectStatus:
    """Data abstraction layer"""
    numbered: bool
    multiple_opposition_unnumbered: bool
    current_opposition_one_opp_unnumbered: bool
    previous_opposition_one_opp_unnumbered: bool
    ignore_brightening_at_solar_elongs_greater_than: int
    ignore_currently_brighter_than: int
    display_labels: bool


@dataclass
class ResultSorting:
    """Data abstraction layer"""
    sort_by: str
    order: str


@dataclass
class MPES:
    """Data abstraction layer"""
    observatory_code: str
    n_of_ephemeris_dates: str
    ephemeris_interval: int
    ephemeris_units: str
    position_units: str
    mode: int
    display: str


@dataclass
class Criteria:
    """Final data abstraction layer"""
    observingDate: ObservingDate
    observability: Observability
    uncertainty: Uncertainty
    objectType: ObjectType
    objectStatus: ObjectStatus
    resultSorting: ResultSorting
    mpes: MPES

# Cookie option?


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
