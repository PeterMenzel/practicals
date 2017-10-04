

from prac_08.car import Car
from random import randint


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_number = randint(0, 100)
        distance_driven = 0
        if self.reliability > random_number:
            distance_driven = super().drive
        return distance_driven
