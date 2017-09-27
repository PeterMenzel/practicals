

from prac_07.guitar import Guitar

CURRENT_YEAR = 2017
VINTAGE_AGE = 50


def main():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    print(guitar)
    print(guitar.get_age())
    print(guitar.is_vintage())

    another_guitar = Guitar("Another Guitar", 2012, 1512.9)
    print(another_guitar)
    print(another_guitar.get_age())
    print(another_guitar.is_vintage())

    print("{} get_age() - Expected {}. Got {}".format(guitar.name, 95, guitar.get_age()))
    print("{} get_age() - Expected {}. Got {}".format(another_guitar.name, 5, another_guitar.get_age()))
    print("{} is_vintage() - Expected {}. Got {}".format(guitar.name, True, guitar.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}".format(another_guitar.name, False, another_guitar.is_vintage()))

main()
