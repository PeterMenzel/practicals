"""Peter"""


def main():
    name = get_name()
    step = get_step()
    print(name[::step])


def get_name():
    name = input("What is your name? ")
    while name == "":
        print("Invalid name!")
        name = input("What is your name?")
    return name


def get_step():
    step = int(input("Choose step size: "))
    return step


main()
