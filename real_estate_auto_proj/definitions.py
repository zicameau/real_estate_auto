import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) # This is your Project Root
CONFIG_PATH = os.path.join(ROOT_DIR, 'configuration.conf')  # requires `import os`
US_STATE_AND_CITIES_PATH =  ROOT_DIR+"/static/US_States_and_Cities.json"
US_CITIES_AND_ZIPCODES_PATH = ROOT_DIR+"/static/USCities.json"
STATE_NAMES_TO_ABBREVIATIONS_PATH = ROOT_DIR+"/static/StateAbbreviationToStateName.json"

