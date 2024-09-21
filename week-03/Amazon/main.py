from amazon import calculate_shipping,calculate_total
# book =
books = [
    {"author": "sanderson", "title": "way of the kings", "price": 10},
    {"author": "sanderson", "title": "second book", "price": 30},
]



command = input("Do you want to checkout: ")
if command != "yes":
    print("Come back soon!")
total = calculate_total(books)
print(f"Your total is {total+calculate_shipping(total)}")
