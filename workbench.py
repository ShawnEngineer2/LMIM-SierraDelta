from turtle import clear
from mimesis.enums import Gender
import data_engine.builders.customerbuilder as CB
import data_engine.builders.builder_errors as blderr
from numpy import random as np_rdm
from os import system as sys


sys("clear")

#for curr_enum in Gender:
#    print(type(curr_enum))
#    print(curr_enum)

#print(np_rdm.choice(Gender))

cb = CB.CustomerBuilder()

new_cust = ""
try:
    new_cust = cb.NewCustomer(cust_type=4, gender=0)

except blderr.InvalidParameterValueError as eIPVE:
    print("Invalid parameter value for parameter ", str(eIPVE))



print(new_cust)





