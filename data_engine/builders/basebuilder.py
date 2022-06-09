#This class is the superclass that all builders inherit from

import data_engine.builders.builder_errors as err
from enum import Enum
from numpy import random as np_rdm

class BaseBuilder(object):
    def __init__(self):
        pass

    def random_from_enum(self, input_enum: Enum)->Enum:
        return np_rdm.choice(input_enum)

    def match_enum_int(self, input_enum:Enum, value_to_find: int)->Enum:
        #Iterate through the enum and if a match is found return it
        for enum in input_enum:
            if enum.value == value_to_find:
                return enum

        #If you get this far, just return None
        return None

    def throw_invalid_parm_value_exception(self, parameter_name:str):
        return err.InvalidParameterValueError(parameter_name)
