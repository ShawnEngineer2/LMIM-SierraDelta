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

class OfficeTypes(enum.Enum):
    unknown = 0
    marineport = 1
    disthub = 2
    railyard = 3
    freightyard = 4
    warehouse = 5
    retail = 6
    corporate = 7
    airport = 8

class OfficeStatus(enum.Enum):
    unknown = 0
    open_public = 1
    open_private = 2
    open_corporate = 3
    closed_general = 4
    closed_capacity = 5
    closed_seasonal = 6
    closed_decommissioned = 7
    





