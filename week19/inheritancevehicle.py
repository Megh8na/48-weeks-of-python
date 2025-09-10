# Week 19: Inheritance with User Input - Vehicle, Bike, Bus

class Vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Color: {self.color}")

class Bike(Vehicle):
    def __init__(self, brand, color, engine_cc):
        super().__init__(brand, color)
        self.engine_cc = engine_cc

    def display_info(self):
        super().display_info()
        print(f"Engine CC: {self.engine_cc}cc")

class Bus(Vehicle):
    def __init__(self, brand, color, seating_capacity):
        super().__init__(brand, color)
        self.seating_capacity = seating_capacity

    def display_info(self):
        super().display_info()
        print(f"Seating Capacity: {self.seating_capacity} passengers")

# Get input from user for Bike
print("Enter Bike Details:")
bike_brand = input("Bike Brand: ")
bike_color = input("Bike Color: ")
bike_cc = int(input("Engine CC: "))
bike1 = Bike(bike_brand, bike_color, bike_cc)

# Get input from user for Bus
print("\nEnter Bus Details:")
bus_brand = input("Bus Brand: ")
bus_color = input("Bus Color: ")
bus_seats = int(input("Seating Capacity: "))
bus1 = Bus(bus_brand, bus_color, bus_seats)

# Print the info
print("\nBike Information:")
bike1.display_info()

print("\nBus Information:")
bus1.display_info()
