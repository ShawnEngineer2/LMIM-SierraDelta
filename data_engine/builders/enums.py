#This module holds all the enumerations used by the data engine
import enum

class CustTypes(enum.Enum):
    unknown = 0
    individual = 1
    business = 2
    enterprise = 3
    government = 4
    education = 5

class VerifyStatus(enum.Enum):
    unknown = 0
    not_verified = 1
    verified = 2
    reverify_needed = 3


