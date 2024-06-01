UP = (0, 1)
RIGHT = (1, 0)
DOWN = (0, -1)
LEFT = (-1, 0)
BLACK = 1
WHITE = 0

def move(position, direction):
    x, y = position
    dx, dy = direction
    return (x+dx, y+dy)

def decide_direction(current_direction, current_color):
    if current_color == BLACK:
        return turn_counter_clockwise(current_direction)
    if current_color == WHITE:
        return turn_clockwise(current_direction)

def advance_state():
    return (1, 0), None, {(0, 0): 1}


def turn_clockwise(direction):
    clockwise_changes = {UP: RIGHT, RIGHT: DOWN, DOWN: LEFT, LEFT: UP}
    return clockwise_changes[direction]


def turn_counter_clockwise(direction):
    counter_clockwise_changes = {UP: LEFT, LEFT: DOWN, DOWN: RIGHT, RIGHT: UP}
    return counter_clockwise_changes[direction]


def updated_ant_state(position, direction, color):
    new_direction = decide_direction(direction, color)
    new_position = move(position, new_direction)
    return new_position, new_direction

