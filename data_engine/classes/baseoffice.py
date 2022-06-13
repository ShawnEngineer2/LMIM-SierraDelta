#This class represents a basic synthetic office record
from datetime import date

class BaseOffice(object):

    office_id: int = 0
    office_name: str = ""
    office_type: int = 0
    office_status: int = 0
    opened_dt: date = None
    closed_dt: date = None
    next_open_dt: date = None
    next_close_dt: date = None
    decommissioned_dt: date = None
    addr_line1: str = ""
    addr_line2: str = ""
    addr_line3: str = ""
    addr_line4: str = ""
    addr_city: str = ""
    addr_country_subdivision: str = ""
    addr_country: str = ""
    addr_country_code: str = ""
    addr_postal_code: str = ""

    def __init__(self):
        pass