# Week 18: Constructors and Methods - Speed Check in Car class

class Car:
    def __init__(self, brand, model, year, speed):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def display_info(self):
        print(f"Car: {self.year} {self.brand} {self.model}, Speed: {self.speed} km/h")

    def check_speed(self):
        if self.speed > 100:
            return "Speeding!"
        else:
            return "Driving safely"

# Create object
car1 = Car("BMW", "X5", 2022, 120)
car2 = Car("Hyundai", "i20", 2023, 85)

# Display info + speed status
car1.display_info()
print(car1.check_speed())

print()  # line break

car2.display_info()
print(car2.check_speed())
