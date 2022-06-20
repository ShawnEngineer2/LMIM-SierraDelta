#This library contains class definitions for random office builder
from datetime import date, datetime
from enum import Enum

from data_engine.builders.basebuilder import BaseBuilder
from data_engine.classes.baseoffice import BaseOffice


class OfficeBuilder(BaseBuilder):

    _local_office_data: list = [] #Note: This dict is a mock data structure for development. Will be replaced after Master Data is up


    def __init__(self):
        #Run the internal routine to create mock office data
        self.gen_mock_data()


    def gen_mock_data(self):
        #This method generates mock data in the class. Temporary only.
        self._local_office_data.append({"office_id": 1, "office_name": "Corp HQ", "office_type": 7, "office_status": 3, "addr_country_code": "USA", "addr_country": "United States of America"})
        self._local_office_data.append({"office_id": 2, "office_name": "Port of Altamira", "office_type": 1, "office_status": 2, "addr_country_code": "MEX", "addr_country": "United Mexican States"})
        self._local_office_data.append({"office_id": 3, "office_name": "Port of Ensenada", "office_type": 1, "office_status": 2, "addr_country_code": "MEX", "addr_country": "United Mexican States"})
        self._local_office_data.append({"office_id": 4, "office_name": "Port of Manzanillo", "office_type": 1, "office_status": 2, "addr_country_code": "MEX", "addr_country": "United Mexican States"})
        self._local_office_data.append({"office_id": 5, "office_name": "Port of Charleston, SC", "office_type": 1, "office_status": 2, "addr_country_code": "USA", "addr_country": "United States of America"})
        self._local_office_data.append({"office_id": 6, "office_name": "Port of Rotterdam", "office_type": 1, "office_status": 2, "addr_country_code": "NLD", "addr_country": "Netherlands"})
        self._local_office_data.append({"office_id": 7, "office_name": "Port of Hamburg", "office_type": 1, "office_status": 2, "addr_country_code": "DEU", "addr_country": "Deutchsland"})
        self._local_office_data.append({"office_id": 8, "office_name": "Jurong Port", "office_type": 1, "office_status": 2, "addr_country_code": "SGP", "addr_country": "Singapore"})
        self._local_office_data.append({"office_id": 9, "office_name": "Laem Chabang Port", "office_type": 1, "office_status": 2, "addr_country_code": "THA", "addr_country": "Thailand"})
        self._local_office_data.append({"office_id": 10, "office_name": "Port of Mumbai", "office_type": 1, "office_status": 2, "addr_country_code": "IND", "addr_country": "Republic of India"})

    def GetOffice(self, office_id: int):
        #Return an existing office. If the office_id doesn't exist return OfficeNotFound error
        
        baseOffice = None

        for office in self._local_office_data:

            if office["office_id"] == office_id:
                #Found office - populate an Office class instance and return it
                baseOffice = BaseOffice()

                baseOffice.office_id = office["office_id"]
                baseOffice.office_name = office["office_name"]
                baseOffice.office_type = office["office_type"]
                baseOffice.office_status = office["office_status"]
                baseOffice.opened_dt = None
                baseOffice.closed_dt = None
                baseOffice.next_open_dt = None
                baseOffice.next_close_dt = None
                baseOffice.decommissioned_dt = None
                baseOffice.addr_line1 = ""
                baseOffice.addr_line2 = ""
                baseOffice.addr_line3 = ""
                baseOffice.addr_line4 = ""
                baseOffice.addr_city = ""
                baseOffice.addr_country_subdivision = ""
                baseOffice.addr_country = office["addr_country"]
                baseOffice.addr_country_code = office["addr_country_code"]
                baseOffice.addr_postal_code = ""

        #Check to see if anything was found and handle appropriately
        if baseOffice == None:
            #No office found - raise an exception
            raise super().throw_office_not_found_exception()

        else:
            return baseOffice

    def GetRandomOffice(self):
        #Returns a random LeMonde office location
        randomOffice: dict = super().random_from_list(self._local_office_data)
        
        return self.GetOffice(randomOffice["office_id"])
