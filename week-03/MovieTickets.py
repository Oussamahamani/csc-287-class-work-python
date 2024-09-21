while True:
    command = input("What is your age: ")
    ticket = None
    if command == "quit": break
    age = int(command)
    if age <3: 
        ticket = "free"
    elif 3 <=age<=12:
        ticket = "$10"
    elif age >12:
        ticket = "$15"
    print(f"your ticket price is {ticket}")