class Car:
    def __init__(self, make, model, sticker_price):
        self.make = make
        self.model = model
        self.sticker_price = sticker_price

    def discount_price(self):
        return self.sticker_price * 0.9

class Sport(Car):
    def __init__(self, make, model, sticker_price, sport_wheels, sport_engine, sport_interior):
        super().__init__(make, model, sticker_price)
        self.sport_wheels = sport_wheels
        self.sport_engine = sport_engine
        self.sport_interior = sport_interior

    def sport_wheels_price(self):
        return 1000.00 if self.sport_wheels == "Y" else 0.00

    def sport_engine_price(self):
        return 3000.00 if self.sport_engine == "Y" else 0.00

    def sport_interior_price(self):
        return 2000.00 if self.sport_interior == "Y" else 0.00

    def pricewithoptions(self):
        return self.discount_price() + self.sport_wheels_price() + self.sport_engine_price() + self.sport_interior_price()

my_sport_car = Sport("Jeep", "Hummer", 70000, "Y", "Y", "Y")

print(f"Make: {my_sport_car.make}")
print(f"Model: {my_sport_car.model}")
print(f"Sticker Price: ${my_sport_car.sticker_price:.2f}")
print(f"Discount Price: ${my_sport_car.discount_price():.2f}")
print(f"Price with Options: ${my_sport_car.pricewithoptions():.2f}")