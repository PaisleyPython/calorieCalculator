# CALORIE CALCULATOR

from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
from selectorlib import Extractor
from pprint import pprint


# This is required if the website doesn't allow python to query the data
headers = {'Accept-Language': "en-GB,en-US;q=0.9,en;q=0.8",
           'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}
# <div class="h2">3&nbsp;°C</div>

URL = "https://www.timeanddate.com/weather/uk/swansea/"


response = requests.get(URL)
webpage = response.text

extractor = Extractor.from_yaml_file(
    "App-6-Project-Calorie-Webapp/temperature.yaml")
temp = float(extractor.extract(webpage)["temp"][0])

print(temp)


# soup = BeautifulSoup(webpage, "html.parser")
# print(response)


app = Flask(__name__)


class CalorieCalculator:

    def __init__(self, weight, height, age, temperature):
        self.temperature = temperature
        self.weight = weight
        self.height = height
        self.age = age

    def calculate(self):
        pass

# @app.route("/"):
# def


# app = CalorieCalculator("86", "186", "36", "10")
# print(app)
