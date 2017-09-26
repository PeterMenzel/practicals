

from prac_07.guitar import Guitar


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

main()
