import datetime
from dataclasses import dataclass


@dataclass
class Criteria:
    """Final data abstraction layer"""
    pass


@dataclass
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
    solar_elong: tuple
    lower_galactic_lat_limit: tuple


@dataclass
class Uncertainty:
    """Data abstraction layer"""
    current_uncertainty: tuple
    consider_sigma: int
    only_show_not_seen_more_than: int


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
    ignore_brightening_at_solar_elongs_greater_than: bool
    ignore_currently_brighter_than: bool
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


@dataclass
class Motions:
    """Data abstraction layer"""
    mode: int
    display: str


# Cookie option?
