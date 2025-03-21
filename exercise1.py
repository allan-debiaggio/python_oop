class Car:
    def __init__(self, brand, model, year):
        """Initialize the car with brand, model, year, and default speed of 0."""
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0  # Default speed is 0 when the car is created

    def accelerate(self, amount):
        """Increase the car's speed by a given amount."""
        self.speed += amount

    def brake(self, amount):
        """Decrease the car's speed by a given amount, but never below 0."""
        self.speed = max(0, self.speed - amount)  # Ensures speed doesn't go negative

    def display_info(self):
        """Print the car's details."""
        print(f"{self.brand} {self.model} ({self.year}) - Speed: {self.speed} km/h")


# Example usage:
my_car = Car("Toyota", "Corolla", 2022)
my_car.display_info()  # Toyota Corolla (2022) - Speed: 0 km/h
my_car.accelerate(30)
my_car.display_info()  # Toyota Corolla (2022) - Speed: 30 km/h
my_car.brake(10)
my_car.display_info()  # Toyota Corolla (2022) - Speed: 20 km/h
my_car.brake(25)
my_car.display_info()  # Toyota Corolla (2022) - Speed: 0 km/h
