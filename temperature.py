
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


# result = Temperature(country="uk", city="swansea")
# print(result.get())

# ============================================================

# This is required if the website doesn't allow python to query the data
# headers = {'Accept-Language': "en-GB,en-US;q=0.9,en;q=0.8",
#            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}
