from room import Room

class Building:
    def __init__(self, name):
        self.name = name
        self.__rooms = []
    
    def add_room(self,number):
         self.__rooms.append(Room(number))
    
    def get_number_rooms(self):
        return len(self.__rooms)