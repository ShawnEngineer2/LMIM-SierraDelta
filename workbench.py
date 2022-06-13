from data_engine.builders.officebuilder import OfficeBuilder
from data_engine.classes import baseoffice
from os import system as sys


sys("clear")

ob = OfficeBuilder()

office: baseoffice = ob.GetRandomOffice()

#office: baseoffice = ob.GetOffice(15)

print(office.office_name)

print("Done")




