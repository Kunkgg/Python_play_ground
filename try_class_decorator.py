class Car:
    wheels = 4
    total = 0

    def __init__(self, name, band):
        self.name = name
        self.band = band
        Car.total += 1

    @staticmethod
    def full_name(name, band):
        return name.upper() + "_" + band.upper()

    @classmethod
    def get_wheels1(cls):
        return cls.wheels

    def get_wheels2(self):
        return Car.wheels

    @classmethod
    def get_total1(cls):
        return cls.total

    def get_total2(self):
        return Car.total


breakpoint()
