# CALORIE CALCULATOR

from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
import requests
from temperature import Temperature

app = Flask(__name__)


class CalorieCalculator:

    def __init__(self, weight, height, age, temperature):
        self.temperature = temperature
        self.weight = weight
        self.height = height
        self.age = age

    def calculate(self):
        result = 10 * self.weight + 6.5 * self.height + 5 - self.temperature * 10
        return result


# country = input("Enter a Country: ")
# city = input("Enter a City: ")
# weight = int(input("Enter your Weight in kg: "))
# height = int(input("Enter your height in CM: "))
# age = int(input("Enter your age: "))

if __name__ == "__main__":
    temperature = Temperature(country="uk", city="swansea").get()
    app = CalorieCalculator(weight=86, height=186,
                            age=36, temperature=temperature)
    print(app.calculate())
