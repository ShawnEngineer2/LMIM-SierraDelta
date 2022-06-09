## This file is the main entry point for the SynthData microservice. This file defines and initalizes endpoints
## then starts the REST server

import uvicorn
from fastapi import FastAPI, APIRouter
from typing import Optional
from http import HTTPStatus
from os import system as sys

from services.customerservice import CustomerService

#Clear the terminal screen
sys("clear")

# Initialize the API server
app = FastAPI(title="SynthDataAPI", openapi_url="/openapi.json")
api_router = APIRouter()

# Configure routing
@api_router.get("/synthdata/NewRandomCustomer/", status_code=HTTPStatus.OK)
def NewRandomCustomer(office_code: Optional[int] = 0, cust_type: Optional[int] = 0, gender: Optional[int] = 0) -> dict:
    """Retrieve New Random Customer from Data Engine"""
    svc = CustomerService()
    return {"data" : svc.new_random_customer(office_code, cust_type, gender)}

@api_router.get("/synthdata/EmptyCustomer/", status_code=HTTPStatus.OK)
def EmptyCustomer() -> dict:
    """Retrieve an empty Customer dataset representation"""
    svc = CustomerService()
    return {"data" : svc.empty_customer()}

@api_router.get("/synthdata/GetRandomCustomer/", status_code=HTTPStatus.OK)
def GetRandomCustomer() -> dict:
    """Retrieve an existing customer from Master Data"""
    return {"data" : "Not Implemented"}

# Add routing to the Web Server
app.include_router(api_router)

# Start the Web Server and stand up the microservice
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001, log_level="debug")

