

def calculate_total(book_list):
    total = 0
    for item in book_list:
        total += item["price"]
    return total


def calculate_shipping(total_price):
    return 0.00 if total_price > 100 else 3.99

