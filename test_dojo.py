import pytest

from dojo import (
    BLACK, DOWN, RIGHT, UP, LEFT, WHITE,
    advance_state,
    move,
    decide_direction,
    turn_clockwise, turn_counter_clockwise, updated_ant_state
)

def test_advance_state_returns_state():
    new_state = advance_state()
    assert new_state is not None


def test_first_step_from_default_state_correct():
    ant_position, _, _ = advance_state()
    assert ant_position == (1, 0)

def test_grid_state_after_first_step_from_default_state():
    _, _, new_grid = advance_state()
    assert new_grid == {(0, 0): 1}

#simulate whole bunch of ant movements

#simulate one step

#figuring out the new direction ant looks at
##turning the ant
def test_update_ant_direction_clockwise():
    assert turn_clockwise(UP) == RIGHT
    assert turn_clockwise(RIGHT) == DOWN

def test_update_ant_direction_counter_clockwise():
    assert UP == turn_counter_clockwise(RIGHT)
    assert RIGHT == turn_counter_clockwise(DOWN)

    #counterclockwise

#figuring out the new pos of the ant
def test_move():
    new_position = move((0, 0), UP)
    assert new_position == (0, 1)
    new_position = move((1, 1), RIGHT)
    assert new_position == (2, 1)


@pytest.mark.parametrize('current_direction,current_color,new_direction',
                         [(UP, BLACK, LEFT),
                          (UP, WHITE, RIGHT),
                          (DOWN, WHITE, LEFT),
                          ])
def test_next_rule(current_direction, current_color, new_direction):
    assert decide_direction(current_direction, current_color) == new_direction


# update ant function
#  - current pos/dir of ant
#  - color of the grid at the position
#  => new position/direction of the ant
def test_updated_ant_state():
    assert updated_ant_state((0, 0), UP, WHITE) == ((1, 0), RIGHT)
    assert updated_ant_state((0, 0), UP, BLACK) == ((-1, 0), LEFT)

#change grid color at a defined pos
def test_toggle_square():
    position = (0,0)
    assert toggle_square({}, position) == {position:BLACK}
