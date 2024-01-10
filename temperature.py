
""" weather to be extracted from timeandate.com/weather"""

import requests
from selectorlib import Extractor


class Temperature:

    def __init__(self, country, city):
        self.country = country
        self.city = city

    def get(self):

        URL = f"https://www.timeanddate.com/weather/{self.country}/{self.city}"
        response = requests.get(URL)
        webpage = response.text

        extractor = Extractor.from_yaml_file(
            "App-6-Project-Calorie-Webapp/temperature.yaml")
        temp = float(extractor.extract(webpage)["temp"][0])
        return temp


result = Temperature(country="uk", city="swansea")
print(result.get())
