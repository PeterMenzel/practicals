


number_of_items = int(input("Number of Items: "))
price_of_item = 0
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of Items: "))
for i in range(0, number_of_items):
    price_of_item = float(input("Price of Item: $")) + price_of_item
if price_of_item > 100:
    price_of_item = price_of_item - (price_of_item * 0.1)

print("Total price for", number_of_items, "items is $", "{:.2f}".format(price_of_item))