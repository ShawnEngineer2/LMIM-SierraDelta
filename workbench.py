from turtle import clear
from mimesis.enums import Gender
#import data_engine.builders.customerbuilder as CB
import traceback as tb
import services.customerservice as svc
import data_engine.builders.builder_errors as blderr
from numpy import random as np_rdm
from os import system as sys


sys("clear")

cs = svc.CustomerService()

new_cust = None
try:
    #new_cust = cb.NewCustomer(cust_type=4, gender=0)
    #new_cust = cs.new_random_customer(office_code=0, cust_type=0, gender=5)

    new_cust = cs.empty_customer()

except Exception as excp:
    tb.print_exception(excp)



print(new_cust)





