# This is the implementation of the customer service endpoints defined in
# main.py at the root of this project
from services.baseservice import BaseService
from data_engine.builders.customerbuilder import CustomerBuilder
from http import HTTPStatus
from fastapi import HTTPException

from datetime import date

class CustomerService(BaseService):
    def __init__(self):
        pass

    def new_random_customer(self, office_code: int, cust_type: int, gender: int)-> dict:
        cb = CustomerBuilder()
        cust_record = None
        try:
            cust_record = cb.NewCustomer(office_code, cust_type, gender)

        except Exception as excp:
            super().exception_handler(excp)

        return cust_record

    def empty_customer(self)-> dict:
        cb = CustomerBuilder()
        cust_record = None
        try:
            cust_record = cb.EmptyCustomer()

            #Load empty record with dummy values
            cust_record.cust_id = 0
            cust_record.first_name = "Empty"
            cust_record.last_name = "Customer"
            cust_record.user_name = "EmptyCustomer123"
            cust_record.setup_date = date.today()
            cust_record.cust_type = 0
            cust_record.addr_line1 = "Empty Address"
            cust_record.addr_line2 = "Empty Address"
            cust_record.addr_line3 = "Empty Address"
            cust_record.addr_line4 = "Empty Address"
            cust_record.addr_city = "Empty City"
            cust_record.addr_country_subdivision = "Empty Subdivision"
            cust_record.addr_country = "Empty Country"
            cust_record.addr_country_code = "XX"
            cust_record.addr_postal_code = "Empty Postal Code"
            cust_record.verify_status = 0

        except Exception as excp:
            super().exception_handler(excp)
 
        return cust_record