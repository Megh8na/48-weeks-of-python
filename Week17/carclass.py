# Week 17: Classes and Objects - Car example

# Step 1: Define the Car class
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Details: {self.year} {self.brand} {self.model}")

# Step 2: Create an object of the Car class
my_car = Car("Toyota", "Camry", 2023)

# Step 3: Print the car details
my_car.display_info()
