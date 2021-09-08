from math import ceil
import sys

def input_validation(input_value : str) -> bool:  #Check if the input is correct
    try:
        int(float(input_value))
    except ValueError:
        return False
    if int(float(input_value)) < 0:
        print("")
        return False
    if float(input_value)%1 != 0:
        return False
    return True

assert input_validation("15") == True
assert input_validation("15.0") == True
assert input_validation("jhjlhl") == False
assert input_validation('15.5') == False


def get_new_augmentation_var_values(width_augmentation_avancement : int, width_augmentation_moment : int, width_augmentation : int) -> tuple: #calculate new values
    width_augmentation_avancement = 0
    width_augmentation_moment += 2
    width_augmentation += 2
    return (width_augmentation_avancement, width_augmentation_moment, width_augmentation)

assert get_new_augmentation_var_values(6, 5, 2) == (0, 7, 4)
assert get_new_augmentation_var_values(4, 8, 6) == (0, 10, 8)

def get_width_last_mini_floor(rank : int) -> int:  #calculate the width of the last mini floor of the pyramide with /\ for space
    height_max_floor, width_mini_floor, width_augmentation, width_augmentation_moment, width_augmentation_avancement = 3, 3, 6, 3, 1
    for i in range(rank):
        for j in range(height_max_floor-1):
            width_mini_floor += 2
        if i == rank-1:
            return width_mini_floor
        if width_augmentation_avancement == width_augmentation_moment:
            width_augmentation_avancement, width_augmentation_moment, width_augmentation = get_new_augmentation_var_values(width_augmentation_avancement, width_augmentation_moment, width_augmentation)
        width_mini_floor, height_max_floor, width_augmentation_avancement = (width_augmentation+ width_mini_floor, height_max_floor+1, width_augmentation_avancement+1)
    return width_mini_floor

assert get_width_last_mini_floor(5) == 71
assert get_width_last_mini_floor(1) == 7


def door_build(width_door : int, rank : int, width_mini_floor : int, mini_floor_advancement : int, door_line) -> str: #create the part of the line with door and the handle
    count = 0
    for i in range(width_door):
        if rank >= 5 and mini_floor_advancement == ceil(((width_mini_floor - 2) / 2) + 1) and count == width_door-2:
            return door_line + '$|'
        door_line += '|'
        count += 1
    return door_line

assert door_build(5, 5, 71, 7, '') == '|||||'
assert door_build(5, 5, 7, 4, '') == '|||$|'


def get_door_part(mini_floor_advancement : int, max_floor_advancemet : int, size_door : int, rank : int, size_floor : int) -> str: #verify if a door build is needed and build this part
    door_part = ""
    if mini_floor_advancement >= 2 and max_floor_advancemet == (rank - 1):
        door_part += door_build(size_door, rank, size_floor, mini_floor_advancement, door_part)
    else:
        door_part += size_door * "*"
    return door_part

assert get_door_part(2, 0, 1, 1, 7) == '|'
assert get_door_part(4, 1, 3, 2, 7) == '|||'


def buid_lines(rank : int, width_mini_floor : int, width_door : int, max_floor_advancement : int, mini_floor_advancement : int, height_max_floor : int) -> str: #build each line of the pyramide
    if max_floor_advancement == 0 and mini_floor_advancement == 0:
        return int((get_width_last_mini_floor(rank) - width_mini_floor + 2) / 2 - 1) * ' ' + '/*\\'
    else:
        return int((get_width_last_mini_floor(rank) - width_mini_floor + 2) / 2 - 1) * ' ' + '/' + int(
            (width_mini_floor - width_door) / 2 - 1) * "*" + get_door_part(mini_floor_advancement, max_floor_advancement,
                                                                           width_door, rank, height_max_floor) + int(
            (width_mini_floor - width_door) / 2 - 1) * "*" + '\\'


assert buid_lines(1, 3, 1, 0, 0, 3) == '  /*\\'
assert buid_lines(1, 5, 1, 0, 1, 3) == ' /***\\'
assert buid_lines(1, 7, 1, 0, 2, 3) == '/**|**\\'


def init_var_build_pyramide() -> tuple: #init vars for build_pyramide()
    height_max_floor = 3
    width_mini_floor = 3
    width_door = 1
    door_augmentation_moment = 1
    door_augmentation_advancement = 1
    width_augmentation = 4
    width_augmentation_moment = 3
    width_augmentation_advancement = 1
    return (height_max_floor, width_mini_floor, width_door, door_augmentation_moment, door_augmentation_advancement, width_augmentation, width_augmentation_moment, width_augmentation_advancement)

assert init_var_build_pyramide() == (3, 3, 1, 1, 1, 4, 3, 1)
assert init_var_build_pyramide() != (6, 2, 5, 4, 5, 2, 4, 1)

def build_pyramide(rank : int) -> str: #build the pyramide
    pyramide = ""
    height_max_floor, width_mini_floor, width_door, door_augmentation_moment, door_augmentation_advancement, augmentation, augmentation_moment, augmentation_advancement = init_var_build_pyramide()
    for max_floor_advancemet in range(rank):
        for mini_floor_advancement in range(height_max_floor):
            pyramide += '\n' + buid_lines(rank, width_mini_floor, width_door, max_floor_advancemet, mini_floor_advancement,
                                   height_max_floor)
            width_mini_floor += 2
        if augmentation_advancement == augmentation_moment:
            augmentation_advancement, augmentation_moment, augmentation = 0, augmentation_moment + 2, augmentation + 2
        if door_augmentation_advancement == door_augmentation_moment:
            door_augmentation_advancement, door_augmentation_moment, width_door = 0, door_augmentation_moment + 2, width_door + 2
        augmentation_advancement, door_augmentation_advancement, width_mini_floor, height_max_floor = augmentation_advancement + 1, door_augmentation_advancement + 1, width_mini_floor + augmentation, height_max_floor + 1
    return pyramide

assert build_pyramide(1) == '\n  /*\\\n /***\\\n/**|**\\'

if len(sys.argv) == 2:
    if input_validation(sys.argv[1]) == True:
        print(build_pyramide(int(float(sys.argv[1]))))
    else:
        print("Please enter a valid value")
else:
    print("Please enter a valid value")
