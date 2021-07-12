class Car:
    wheels = 4

    def __init__(self, color, model, year):
        self.color = color
        self.model = model
        self.year = year
        self.__cups = 40


def main():
    car = Car("red", "BYD", 2021)
    car3 = Car("yellow", "BYD", 1900)
    print(f"{car.color} {car.model} {car.year} {car.wheels}")
    print(f"{Car.wheels}")
    print('=' * 20)
    car.wheels = 8
    print(f"{car.color} {car.model} {car.year} {car.wheels}")
    print(f"{Car.wheels}")
    print('=' * 20)
    Car.wheels = 6
    print(f"{car.color} {car.model} {car.year} {car.wheels}")
    print(f"{Car.wheels}")
    car2 = Car("white", "Benze", 2000)
    print(f"{car2.color} {car2.model} {car2.year} {car2.wheels}")
    print(f"{Car.wheels}")
    print(f"{car3.color} {car3.model} {car3.year} {car3.wheels}")
    breakpoint()


if __name__ == "__main__":
    main()
