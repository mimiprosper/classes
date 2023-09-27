class House():
    def __init__(self, color, floor_type, no_rooms, roof_type, size) -> None:
        self.color = color
        self.floor_type = floor_type
        self.no_rooms = no_rooms
        self.roof_type = roof_type
        self.size = size

class Duplex(House):
    def __init__(self, color, floor_type, no_rooms, roof_type, size) -> None:
        super().__init__(color, floor_type, no_rooms, roof_type, size)
    
    def kitchen():
        print('we can cook')

    def bathroom(self):
        print('we can have bath here')

# create an objec of class duplex
my_house = Duplex('blue', 'tiled', 10, 'aluminium', 'big')
