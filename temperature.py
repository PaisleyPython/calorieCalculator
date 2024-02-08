import requests
from selectorlib import Extractor


class Temperature:

    def __init__(self, country, city):
        self.country = country.replace(" ", "-")
        self.city = city.replace(" ", "-")

    def build_url(self):
        return f"https://www.timeanddate.com/weather/{
            self.country}/{self.city}"

    def get(self):
        url = self.build_url()
        response = requests.get(url).text
        extractor = Extractor.from_yaml_file(
            "App-6-Project-Calorie-Webapp/temperature.yaml")
        scraped_content = float(extractor.extract(response)["temp"][:2])
        return scraped_content


# if __name__ == "__main__":
#     #     result = Temperature(country="usa", city="san francisco")
#     #     print(result.get())
#     result = Temperature(country="usa", city="boston")
#     print(result)
# # #
#
#
#
# NOTES ============================================================

# Having this if __name__ code, prevents the script from being automaticall called when imported
# in another module.
# if __name__ == "__main__":

# This is required if the website doesn't allow python to query the data
# headers = {'Accept-Language': "en-GB,en-US;q=0.9,en;q=0.8",
#            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}
