
"""Peter"""

valid_name = False
name = input("What is your name? ")
while not valid_name:
    if len(name) > 0:
        valid_name = True
    else:
        name = input("What is your name?")
print(name[1::2])
