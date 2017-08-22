name = input("What is your name? ")
NAME_FILE = "name.txt"
name_file = open(NAME_FILE, 'w')
print(name, file=name_file)
name_file.close()

name_file = open(NAME_FILE, 'r')
name = name_file.read()
print("Your name is", name)
name_file.close()

numbers_file = open("numbers.txt", 'r')
total = 0
for line in numbers_file:
    number = int(line)
    total += number
print(total)
numbers_file.close()
