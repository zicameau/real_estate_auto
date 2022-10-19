import random
import time
import sys
import json
import pathlib 

import usaddress

from .definitions import US_STATE_AND_CITIES_PATH, US_CITIES_AND_ZIPCODES_PATH, STATE_NAMES_TO_ABBREVIATIONS_PATH

random.seed(time.time())

class ImproperPropertyInitializationException(Exception):
    pass

class InvalidPropertyKwarg(Exception):
    pass

class InvalidUSStateError(Exception):
    pass

class InvalidCountyError(Exception):
    pass

class InvalidCityError(Exception):
    pass

class InvalidZipCodeError(Exception):
    pass


class InvalidStreetError(Exception):
    pass

class Property:

    """ 
        This is a class that is used to analyze United States Real Estate Properties for further analysis to determine if they are good deals or not. A lot of the process for determining the viability of the property is repetitive and monotonous. These set of tools is to automate this process to help speed up the process of identifying, analyzing and determining whether or not they are viable rentals or investments.
    """

    VALID_KWARGS = [
            'sqft',
            'beds',
            'baths'
            ]

    def __init__(self,  address: str, units: list = None, **kwargs): 
        self.address = address
        tagged_address = usaddress.tag(address)



        self.validate_parameters(tagged_address, units, **kwargs)

        # Validate kwargs that are provided are valid
        for kwarg in kwargs:
            if kwarg not in self.VALID_KWARGS:
                raise InvalidPropertyKwarg(f"Kwarg {kwarg} is invalid, please only use kwargs from the list of valid kwargs:{self.VALID_KWARGS}")

        if units == None:
            if kwargs.get('sqft') == None or kwargs.get('baths') == None or kwargs.get('beds') == None:
                raise ImproperPropertyInitializationException("If no units provided, sqft, beds and baths required parameters")
            self.__set_units([Property_Unit(kwargs.get('sqft'), kwargs.get('beds'), kwargs.get('baths'))])
        else:
            self.__set_units(units)


    def validate_parameters(self, tagged_address, units, **kwargs):
        """
            Validates the data that is provided by the object is valid and if it is not then
            this function will throw the appropriate error for whichever error that it ran into. 
        """


        states_to_cities = None
        all_zipcodes = None
        names_to_abbrevs = None
        with open(US_STATE_AND_CITIES_PATH) as states_and_cities_file:
            states_to_cities = json.load(states_and_cities_file)

        with open(US_CITIES_AND_ZIPCODES_PATH) as zipcodes_file:
            all_zipcodes = json.load(zipcodes_file)

        with open(STATE_NAMES_TO_ABBREVIATIONS_PATH) as names_to_abbrevs_file:
            names_to_abbrevs = json.load(names_to_abbrevs_file)

        abbrevs_to_names = {}
        for name in names_to_abbrevs:
            abbrevs_to_names[names_to_abbrevs[name]] = name

        # Get the necesary items from the address
        zip_code = None
        state = None
        for val in tagged_address:
            if val[0] == 'StateName':
                state = val[1]
            elif val[0] == 'ZipCode':
                zip_code = val[1]
            elif val[0] == ''

        if state == None:
            raise InvalidUSStateError(f"Could not identify state in tagged address {tagged_address}")

        # Convert state to a name if the name is an abbreviation instead
        if len(state) == 2:
            state = abbrevs_to_names.get(state)

        if names_to_abbrevs.get(state) == None:
            raise InvalidUSStateError(f"The state provided {state} does not exist")

        found_zip = False
        for elem in all_zipcodes:
            if str(elem.get("zip_code")) == zip_code:
                found_zip = True
                if elem.get("city") != city:
                    raise InvalidCityError(f"City {city} is not associated with the zipcode {zip_code}")
                if elem.get("state") != names_to_abbrevs[state]:
                    raise InvalidUSStateError(f"State {state} is not associated with the zipcode {zipcode}")
                if elem.get("county") != county:
                    raise InvalidCountyError(f"County {county} is not associated with the zipcode {zip_code}")
        if found_zip == False:
            raise InvalidZipCodeError(f"Zip code {zip_code} provided is invalid")




    def get_units(self):
        return self.units

    def get_street_address(self):
        return self.street_addr

    def get_city(self):
        return self.city

    def get_state(self):
        return self.state

    def get_county(self):
        return self.county

    def get_apt_unit(self):
        return self.apt_unit

    def get_zip_code(self):
        return self.zip_code
    
    def __set_units(self, units):
        self.units = units

    def __set_street_address(self, street_address):
         self.street_addr = street_address

    def __set_city(self, city):
         self.city = city

    def __set_state(self, state):
         self.state = state

    def __set_county(self, county):
         self.county = county

    def __set_apt_unit(self, apt_unit):
         self.apt_unit = apt_unit

    def __set_zip_code(self, zip_code):
         self.zip_code = zip_code

    def get_address(self):
        if self.apt_unit == None:
            return self.ADDRESS_FORMAT_STRING_NO_APT
        else:
            return self.ADDRESS_FORMAT_STRING_WITH_APT


    def get_total_rooms(self):
        num_rooms = 0
        for unit in self.units:
            num_rooms = num_rooms + unit.get_beds()
        return num_rooms

    def get_total_baths(self):
        num_baths = 0
        for unit in self.units:
            num_baths = num_baths + unit.get_baths()
        return num_baths

    def get_total_sqft(self):
        sqft = 0
        for unit in self.units:
            sqft = sqft + unit.get_sqft()
        return sqft

    def add_unit(self, property_unit):
        self.units = self.units + [property_unit]

    def get_current_total_rent(self):
        rent = 0
        for unit in self.units:
            rent = rent + unit.get_current_rent()
        return rent

    def get_current_total_market_rent(self):
        rent = 0
        for unit in self.units:
            rent = rent + unit.get_current_market_rent()
        return rent




class Property_Unit:
    """
        This is a unit within a piece of property. AKA it is the thing that
        would be rented out. These have bedrooms and bathrooms
    """

    def __init__(self, sqft, beds, baths, current_rent = 0, current_market_rent=0):
        self.__set_sqft(sqft)
        self.__set_beds(beds)
        self.__set_baths(baths)
        self.__set_id(random.randint(0, sys.maxsize))
        self.set_current_rent(current_rent)
        self.set_current_market_rent(current_market_rent)

    def __set_beds(self, beds):
        self.beds = beds

    def __set_baths(self, baths):
        self.baths = baths

    def __set_sqft(self, sqft):
        self.sqft = sqft

    def __set_id(self, unit_id):
        self.id = unit_id

    def set_current_rent(self, current_rent):
        self.current_rent = current_rent

    def set_current_market_rent(self, current_market_rent):
        self.current_market_rent = current_market_rent

    def get_baths(self):
        return self.baths

    def get_beds(self):
        return self.beds

    def get_sqft(self):
        return self.sqft

    def get_id(self):
        return self.id

    def get_current_rent(self):
        return self.current_rent

    def get_current_market_rent(self):
        return self.current_market_rent


class ProForma:
    """
        What is a proforma? 

        A proforma is what real estate investors use in order to evaluate a property. It contains
        all of the technical analysis that they need in order to determine whether or not a property
        is a good investment or not. The proforma contains all of the annulaized rents, all of the
        operating expenses of the property, the Annualized ROI, the asking price of the property, the
        asking price for the property. Then with that information the proforma then calculates the 
        cap rate for the property with and without current market rents.
    """

    def __init__(self, asking_price: float, real_property: Property):
        self.asking_price = asking_price
        self.real_property = real_property
