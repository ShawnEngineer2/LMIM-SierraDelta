from datetime import date, datetime
from enum import Enum

import mimesis
from data_engine.builders.basebuilder import BaseBuilder
from data_engine.classes.basecustomer import BaseCustomer
from mimesis import Person, Address, Datetime
from mimesis.locales import Locale 
from mimesis.enums import Gender
from data_engine.builders.builder_enums import CustTypes
from data_engine.builders.builder_enums import VerifyStatus

class CustomerBuilder(BaseBuilder):

    def __init__(self):
        pass


    def NewCustomer(self, office_code: int = 0, cust_type: int = 0, gender: int = 0):
        #Instantiate Mimesis objects
        mp = Person()
        ma = Address()
        md = mimesis.Datetime()

        #Determine the gender of the new customer
        new_cust_gender: Enum = None

        if gender == 0:
            #generate a random gender
            new_cust_gender = super().random_from_enum(Gender)

        elif gender == 1:
            #Female gender
            new_cust_gender = Gender.FEMALE

        elif gender == 2:
            #Male gender
            new_cust_gender = Gender.MALE

        else:
            raise super().throw_invalid_parm_value_exception("gender")
        
        #Determine the customer type for the new customer
        new_cust_type: Enum = None

        if cust_type == 0:
            #generate a random customer type
            new_cust_type = super().random_from_enum(CustTypes)

        else:
            #iterate through the Customer Types enum and match the
            #passed value
            new_cust_type = super().match_enum_int(CustTypes, cust_type)

            if new_cust_type == None:
                #Nothing was matched - throw an error
                raise super().throw_invalid_parm_value_exception("cust_type")
        
        #Determine the verification type for the new customer
        new_cust_verify_status = super().random_from_enum(VerifyStatus)
        
        #Initialize the New Customer object
        baseCustomer = BaseCustomer()

        baseCustomer.cust_id=0
        baseCustomer.first_name=mp.first_name(gender=new_cust_gender)
        baseCustomer.last_name=mp.last_name(gender=new_cust_gender)
        baseCustomer.user_name=mp.username(mask="l_l_d", drange=(1900,6000))
        baseCustomer.setup_date = md.date(start=2017, end=2022)
        baseCustomer.cust_type=new_cust_type.value
        baseCustomer.addr_line1=ma.address()
        baseCustomer.addr_line2=""
        baseCustomer.addr_line3=""
        baseCustomer.addr_line4=""
        baseCustomer.addr_city=ma.city()
        baseCustomer.addr_country_subdivision=ma.state()
        baseCustomer.addr_country=ma.country()
        baseCustomer.addr_country_code=ma.country_code()
        baseCustomer.addr_postal_code=ma.postal_code()
        baseCustomer.verify_status=new_cust_verify_status.value

        return baseCustomer

    def EmptyCustomer(self):
        return BaseCustomer()

    def GetCustomer(self, cust_id:int):
        pass

    def TrySomething(self):
        my_list = super().random_from_enum(Gender)
        print(my_list)


