from src.robot import Robbot, Orientation, Position


class MarsGround:
    def __init__(self):
        self.min_ground_position = 0
        self.max_ground_position = 5

    def has_collided(self, position: Position):
        collided = position.coordinate_x > self.max_ground_position\
                   or position.coordinate_x < self.min_ground_position \
                   or position.coordinate_y > self.max_ground_position\
                   or position.coordinate_y < self.min_ground_position

        return collided


class Mars:
    def __init__(self):
        self.ground = MarsGround()
        self.robbot = Robbot()

    def move(self, command):
        if command == 'right':
            self.robbot.turn_right()
        elif command == 'left':
            self.robbot.turn_left()
        elif command == 'move':
            collided = self.ground.has_collided(self.robbot.position)
            if not collided:
                self.robbot.move()
            else:
                print(f"Comando inválido, o robô irá cair de marte!")

    def change_mars_robbot_position(self, command_list):
        command_position_or = command_list.split(",")
        position_x = int(command_position_or[0])
        position_y = int(command_position_or[1])
        orientation = str(command_position_or[2])

        orientation = Orientation.from_str(orientation)
        self.robbot.position.coordinate_y = position_y
        self.robbot.position.coordinate_x = position_x
        self.robbot.orientation = orientation

    def robbot_report(self):
        return f"{self.robbot.position.coordinate_x},{self.robbot.position.coordinate_y}, {self.robbot.orientation.value}".upper()

