#This is the base class that all services inherit from
import data_engine.builders.builder_errors as blderr
from http import HTTPStatus
from fastapi import HTTPException

class BaseService(object):
    def __init__(self):
        pass

    def exception_handler(self, excp: Exception):
        #Evaluate the type of the incoming exception and handle as needed

        if type(excp) == blderr.InvalidParameterValueError:
            msg: str = "Invalid Value for Parameter: " + excp.parameter_name
            raise HTTPException(status_code = HTTPStatus.BAD_REQUEST, detail = msg)

        else:
            raise excp

