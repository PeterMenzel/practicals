

from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    fancy_car = SilverServiceTaxi("my_fancy_car", 100, 2)
    fancy_car.drive(18)
    print(fancy_car)
    print("${:.2f}".format(fancy_car.get_fare()))


main()