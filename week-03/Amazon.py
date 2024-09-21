# book = 
books = [
{
    "author":'sanderson',
    "title":"way of the kings",
    "price":10
},
{
    "author":'sanderson',
    "title":"second book",
    "price":30
}
]

def calculate_total(book_list):
    total = 0
    for item in book_list:
        total += item["price"]
    return total

def calculate_shipping(total_price):
    return 0.00 if total_price >100 else 3.99


command = input("Do you want to checkout: ")    
if command !="yes":
    print("Come back soon!")
total= calculate_total(books) 
print(f"Your total is {total+calculate_shipping(total)}")