from temperature import Temperature


class CalorieCalculator:

    def __init__(self, weight, height, age, temperature):
        self.temperature = temperature
        self.weight = weight
        self.height = height
        self.age = age

    def calculate(self):
        result = (10 * self.weight + 6.5 *
                  self.height + 5 - self.temperature * 10)
        return result


# if __name__ == "__main__":
#     temperature = Temperature(country=country, city=city).get()
#     app = CalorieCalculator(weight=86, height=186,
#                             age=36, temperature=temperature)
#     print(app.calculate())

#
#
#
# ADDiTIONAL FIELDS ====================================

# country = input("Enter a Country: ")
# city = input("Enter a City: ")
# weight = int(input("Enter your Weight in kg: "))
# height = int(input("Enter your height in CM: "))
# age = int(input("Enter your age: "))
