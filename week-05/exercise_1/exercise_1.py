from building import Building



building0 = Building("Empire State Building")
building0.add_room("251")
building0.add_room("252")
print(f"Number of rooms in building:  {building0.get_number_rooms()}")

building0.__rooms = []
print(building0.__rooms)