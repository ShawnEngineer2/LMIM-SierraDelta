# This is the implementation of the customer service endpoints defined in
# main.py at the root of this project
from data_engine.builders.customerbuilder import CustomerBuilder

class CustomerService(object):
    def __init__(self):
        pass

    def new_random_customer(self, office_code: int, cust_type: int, gender: int)-> dict:
        cb = CustomerBuilder()
        return cb.NewCustomer(office_code, cust_type, gender)

    def empty_customer(self)-> dict:
        cb = CustomerBuilder()
        return cb.EmptyCustomer()