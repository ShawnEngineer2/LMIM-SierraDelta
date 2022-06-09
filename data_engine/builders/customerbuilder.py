from datetime import date, datetime

import mimesis
from data_engine.classes.basecustomer import BaseCustomer
from mimesis import Person, Address, Datetime
from mimesis.locales import Locale 
from mimesis.enums import Gender
from data_engine.builders.enums import CustTypes
from data_engine.builders.enums import VerifyStatus

class CustomerBuilder(object):

    def __init__(self):
        pass


    def NewCustomer(self, office_code: int = 0, cust_type: int = 0, gender: int = 0):
        #Instantiate Mimesis objects
        mp = Person()
        ma = Address()
        md = mimesis.Datetime()
        
        #Initialize the New Customer object
        baseCustomer = BaseCustomer()

        baseCustomer.cust_id=0
        baseCustomer.first_name=mp.first_name(gender=Gender.FEMALE)
        baseCustomer.last_name=mp.last_name(gender=Gender.FEMALE)
        baseCustomer.user_name=mp.username(mask="l_l_d", drange=(1900,6000))
        baseCustomer.setup_date = md.date(start=2017, end=2022)
        baseCustomer.cust_type=CustTypes.unknown
        baseCustomer.addr_line1=ma.address()
        baseCustomer.addr_line2=""
        baseCustomer.addr_line3=""
        baseCustomer.addr_line4=""
        baseCustomer.addr_city=ma.city()
        baseCustomer.addr_country_subdivision=ma.state()
        baseCustomer.addr_country=ma.country()
        baseCustomer.addr_country_code=ma.country_code()
        baseCustomer.addr_postal_code=ma.postal_code()
        baseCustomer.verify_status=VerifyStatus.unknown

        return baseCustomer

    def EmptyCustomer(self):
        return BaseCustomer()

    def GetCustomer(self, cust_id:int):
        pass


