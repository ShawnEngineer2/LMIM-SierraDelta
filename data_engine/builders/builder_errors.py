#This module contains custom errors for builders

class InvalidParameterValueError(Exception):

    parameter_name:str = ""

    def __init__(self, parameter_name:str):
        self.parameter_name = parameter_name

