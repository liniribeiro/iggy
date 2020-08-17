from enum import Enum


class Orientation(Enum):
    north = 'north'
    south = 'south'
    east = 'east'
    west = 'west'

    @staticmethod
    def from_str(label):
        if label:
            label = label.lower()
            try:
                return Orientation[label]
            except Exception as e:
                print(f"{label} não é uma orientação válida!")


class Position:
    def __init__(self, x=0, y=0):
        self.coordinate_x = x
        self.coordinate_y = y


class Robbot:
    def __init__(self):
        self.position = Position()
        self.orientation = Orientation.north
        self.right_orientation = {
            'south': Orientation.west,
            'north': Orientation.east,
            'east': Orientation.south,
            'west': Orientation.north
        }

        self.left_orientation = {
            'south': Orientation.east,
            'north': Orientation.west,
            'east': Orientation.north,
            'west': Orientation.south
        }

    def turn_right(self):
        self.orientation = self.right_orientation[self.orientation.name]

    def turn_left(self):
        self.orientation = self.left_orientation[self.orientation.name]

    def move(self):
        if self.orientation == Orientation.south:
            self.position.coordinate_y = self.position.coordinate_y + 1
        elif self.orientation == Orientation.north:
            self.position.coordinate_y = self.position.coordinate_y - 1
        elif self.orientation == Orientation.east:
            self.position.coordinate_x = self.position.coordinate_x + 1
        elif self.orientation == Orientation.west:
            self.position.coordinate_x = self.position.coordinate_x - 1
