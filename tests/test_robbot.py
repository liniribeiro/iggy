from src.robot import Robbot, Orientation


def test_turn_right():
    robbot = Robbot()
    robbot.turn_right()
    assert robbot.orientation == Orientation.east


def test_turn_left():
    robbot = Robbot()
    robbot.turn_left()
    assert robbot.orientation == Orientation.west


def test_moce_to_south():
    robbot = Robbot()
    robbot.orientation = Orientation.south
    robbot.move()
    assert robbot.position.coordinate_y == 1


def test_moce_to_north():
    robbot = Robbot()
    robbot.orientation = Orientation.north
    robbot.move()
    assert robbot.position.coordinate_y == -1


def test_moce_to_east():
    robbot = Robbot()
    robbot.orientation = Orientation.east
    robbot.move()
    assert robbot.position.coordinate_x == 1


def test_moce_to_west():
    robbot = Robbot()
    robbot.orientation = Orientation.west
    robbot.move()
    assert robbot.position.coordinate_x == -1

