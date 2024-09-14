user1 = {
    "userID": "f8f7f",
    "firstName": "adam",
    "lastName": "smith",
    "email": "adam@gmail.com",
    "address": "boston",
}
user2 = {
    "userID": "dsffd8",
    "firstName": "Sarah",
    "lastName": "John",
    "email": "Sarah@gmail.com",
    "address": "NY",
}
user3 = {
    "userID": "tr78et",
    "firstName": "bob",
    "lastName": "jelo",
    "email": "bob@gmail.com",
    "address": "Washington",
}


users = {
    user1["userID"]: user1,
    user2["userID"]: user2,
    user3["userID"]: user3,
}


for key, value in users.items():
    name = value["firstName"] + " " + value["lastName"]
    print(f"name: {name}, address: {value["address"]}")
