# -*- coding: utf-8 -*-

from context import real_estate_auto_proj

import unittest


class PropertyTestSuite(unittest.TestCase):
    """Basic test cases."""
    beds = 2
    baths = 2
    sqft = 500
    street = "Test_Street"
    zip_code = "62353"
    city = "Mount Sterling"
    state = "IL"
    apt = "Test_Apt"
    county = "Brown"
    current_rent = 500
    current_market_rent = 600

    us_address = "15 E Railroad St, Mount Sterling, IL 62353"

    bad_street = "Test_Street"
    bad_zip_code = "Test_Zip"
    bad_city = "Test_City"
    bad_state = "Test_State"
    bad_apt = "Test_Apt"
    bad_county = "Test_County"

    def test_initializations(self):

        # Test for initialization of property where the property only has one unit and no property units are provided to the property object 
        prop = real_estate_auto_proj.Property(address=self.us_address, beds=self.beds, baths=self.baths, sqft=500)

        # Test for initialziation of a property object with a list of property units
        prop_units = [real_estate_auto_proj.Property_Unit(beds=self.beds, baths=self.baths, sqft=500)]
        prop = real_estate_auto_proj.Property(address=self.us_address, units= prop_units)

        # Test for failure of initialization with no units or beds, baths, or sqft keywords
        try:
            prop = real_estate_auto_proj.Property(self.street, self.zip_code, self.city, self.state, apt_unit=self.apt, county=self.county)
            raise Exception("Failed to successfully fail to not use the beds, baths, or sqft keywords")
        except real_estate_auto_proj.ImproperPropertyInitializationException:
            pass

        # Test for failure with only beds keyword
        try:
            prop = real_estate_auto_proj.Property(address=self.us_address, beds=self.beds)
            raise Exception("Failed to successfully fail using the beds keyword only")
        except real_estate_auto_proj.ImproperPropertyInitializationException:
            pass
            
        # Test for failure with only baths keyword
        try:
            prop = real_estate_auto_proj.Property(address=self.us_address, baths=self.baths)
            raise Exception("Failed to successfully fail using the baths keyword only")
        except real_estate_auto_proj.ImproperPropertyInitializationException:
            pass

        # Test for failure with only sqft keyword
        try:
            prop = real_estate_auto_proj.Property(address=self.us_address, sqft=self.sqft)
            raise Exception("Failed to successfully fail using the sqft keyword")
        except real_estate_auto_proj.ImproperPropertyInitializationException:
            pass

        # Test for failure with only beds, baths keywords
        try:
            prop = real_estate_auto_proj.Property(address=self.us_address, beds=self.beds, baths=self.baths)
            raise Exception("Failed to successfully fail using the beds and baths keywords")
        except real_estate_auto_proj.ImproperPropertyInitializationException:
            pass

        # Test for failure with only beds, sqft keywords
        try:
            prop = real_estate_auto_proj.Property(address=self.us_address, beds=self.beds, sqft=self.sqft)
            raise Exception("Failed to successfully fail using just beds and sqft keywords")
        except real_estate_auto_proj.ImproperPropertyInitializationException:
            pass

        # Test for failure with only baths, sqft keywords
        try:
            prop = real_estate_auto_proj.Property(address=self.us_address, baths=self.baths, sqft=self.sqft)
            raise Exception("Failed to successfully fail using just baths and sqft keywords")
        except real_estate_auto_proj.ImproperPropertyInitializationException:
            pass

        # Test for failure with only baths, sqft keywords
        try:
            prop = real_estate_auto_proj.Property(address=self.us_address, baths=self.baths, sqft=self.sqft)
            raise Exception("Failed to successfully fail using a just baths and sqft keywords")
        except real_estate_auto_proj.ImproperPropertyInitializationException:
            pass


    def test_get_functions(self):

        prop_unit = real_estate_auto_proj.Property_Unit(beds=self.beds, baths=self.baths, sqft=self.sqft)
        prop_unit.set_current_rent(self.current_rent)
        prop_unit.set_current_market_rent(self.current_market_rent)

        prop_units = [prop_unit]
        prop = real_estate_auto_proj.Property(address=self.us_address, units= prop_units)


        prop_no_apt = real_estate_auto_proj.Property(self.street, self.zip_code, self.city, self.state, county=self.county, units= prop_units)

        assert prop.get_total_rooms() == self.beds
        assert prop.get_total_baths() == self.baths
        assert prop.get_total_sqft() == self.sqft
        assert prop.get_current_total_rent() == self.current_rent
        assert prop.get_current_total_market_rent() == self.current_market_rent
        assert prop.get_units()[0] == prop_unit
        assert prop.get_street_address() == self.street
        assert prop.get_city() == self.city
        assert prop.get_state() == self.state
        assert prop.get_county() == self.county
        assert prop.get_apt_unit() == self.apt
        
        assert prop.get_address() == prop.ADDRESS_FORMAT_STRING_WITH_APT 
        assert prop_no_apt.get_address() == prop_no_apt.ADDRESS_FORMAT_STRING_NO_APT


    def test_set_functions(self):

        prop_unit = real_estate_auto_proj.Property_Unit(beds=self.beds, baths=self.baths, sqft=self.sqft)
        prop_unit.set_current_rent(self.current_rent)
        prop_unit.set_current_market_rent(self.current_market_rent)

        prop_units = [prop_unit]
        prop = real_estate_auto_proj.Property(address=self.us_address, units= prop_units)


        prop_no_apt = real_estate_auto_proj.Property(self.street, self.zip_code, self.city, self.state, county=self.county, units= prop_units)

        new_prop_unit = real_estate_auto_proj.Property_Unit(beds=self.beds+1, baths=self.baths+1, sqft=self.sqft+20)
        prop.add_unit(new_prop_unit)


class Property_UnitTestSuit(unittest.TestCase):


    def test_initializations(self):
        prop_unit = real_estate_auto_proj.Property_Unit(beds=1, baths=1, sqft = 500)

    def test_get_functions(self):
        beds = 1
        baths = 1
        sqft = 500

        prop_unit = real_estate_auto_proj.Property_Unit(beds=beds, baths=baths, sqft = sqft)

        assert prop_unit.get_baths() == baths
        assert prop_unit.get_beds() == beds
        assert prop_unit.get_sqft() == sqft
        assert type(prop_unit.get_id()) == int
        assert prop_unit.get_current_rent() == 0
        assert prop_unit.get_current_market_rent() == 0

    def test_set_functions(self):
        prop_unit = real_estate_auto_proj.Property_Unit(beds=1, baths=1, sqft = 500)

        # Test that the public set methods are public
        rent = 500
        prop_unit.set_current_market_rent(rent)
        assert prop_unit.get_current_market_rent() == rent

        curr_rent = 600
        prop_unit.set_current_rent(curr_rent)
        assert prop_unit.get_current_rent() == curr_rent

        # Test that the private set methods are private
        new_beds = 2
        try:
            prop_unit.set_beds(new_beds)
        except AttributeError:
            pass

        new_baths = 2
        try:
            prop_unit.set_baths(new_baths)
        except AttributeError:
            pass


        new_sqft = 2
        try:
            prop_unit.set_sqft(new_sqft)
        except AttributeError:
            pass

        new_id = 2
        try:
            prop_unit.set_id(new_id)
        except AttributeError:
            pass

if __name__ == '__main__':
    unittest.main()
