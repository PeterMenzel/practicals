"""
CP1404/CP5632 Practical
Colour names in a dictionary
"""


COLOUR_NAMES_AND_CODE = {"AliceBlue": "#f0f8ff", "AntiqueWhite4": "#8b8378", "aquamarine1": "#7fffd4", "azure1": "#f0ffff",
               "beige": "#f5f5dc", "black": "#000000", "blue1": "#0000ff", "brown": "#a52a2a", "burlywood": "#deb887", "CadetBlue": "#5f9ea0"}

colour = input("Enter colour name: ")
while colour != "":
    if colour in COLOUR_NAMES_AND_CODE:
        print(colour, "has code", COLOUR_NAMES_AND_CODE[colour])
    else:
        print("Invalid colour name")
    colour = input("Enter colour name: ")

for colour in COLOUR_NAMES_AND_CODE:
    print("{:14} has code {}".format(colour, COLOUR_NAMES_AND_CODE[colour]))
