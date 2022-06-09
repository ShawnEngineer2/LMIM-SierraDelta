#This class represents a basic synthetic customer record. 
from datetime import date, datetime

class BaseCustomer(object):

    cust_id: int = 0
    first_name: str = ""
    last_name: str = ""
    user_name: str =  ""
    setup_date: date
    cust_type: int = 0
    addr_line1: str = ""
    addr_line2: str = ""
    addr_line3: str = ""
    addr_line4: str = ""
    addr_city: str = ""
    addr_country_subdivision: str = ""
    addr_country: str = ""
    addr_country_code: str = ""
    addr_postal_code: str = ""
    verify_status: int = 0

    def __init__(self):
        pass

    