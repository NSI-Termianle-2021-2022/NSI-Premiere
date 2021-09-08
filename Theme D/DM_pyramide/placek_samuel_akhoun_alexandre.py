from math import floor, ceil
import sys

MODE = "prod"

def main() -> str:
    if len(sys.argv) > 1:
        ret = handle_input(sys.argv[1])
        if ret == -1:
            print(f"Entrée incorrecte: {sys.argv[1]}. Vous devez saisir un entier naturel")
        else:
            if ret == 0:
                return ""
            else:
                lines = build_pyramide(ret)
                for i in lines:
                    print(i, end="")
    else:
        print("Vous devez passer un nombre en paramètre")

def build_pyramide(n : int) -> list:
    mini_floor_width = 3
    floor_height = 3
    lines = []
    spacing = int(floor(last_line_width(n) / 2) - 1)
    line_pattern = "/\\"
    star_number = 1
    star_increase = 0
    nber_passages1 = 1
    nber_passages2 = 1
    nber_passages3 = 1
    for i in range(n - 1):
        var = floor_offset(nber_passages1, nber_passages2, nber_passages3, floor_height, star_increase, spacing)
        nber_passages1 = var[0]
        nber_passages2 = var[1]
        nber_passages3 = var[2]
        star_increase = var[3]
        spacing = var[4]
        for j in range(1, floor_height + 1):
            build_single_line(lines, spacing, line_pattern, star_number, star_increase)
            star_number += 2
            spacing -= 1
        floor_height += 1
        star_increase += 4
        spacing -= 2
    build_last_floor(n, nber_passages1, nber_passages2, nber_passages3, lines, spacing, line_pattern, star_number, star_increase, floor_height)
    return lines

def handle_input(input : str) -> int:
    try:
        i = int(float(input))
    except:
        return -1
    else:
        if i < 0:
            return -1
        if i == 0:
            return ""
        return i

def last_line_width(n : int) -> int:
    floor_height = 3
    line_pattern = "/\\"
    star_number = 1
    star_increase = 0
    count1 = 1
    count2 = 1
    count3 = 1

    for i in range(n):
        while floor_height > 5 and floor_height % 3 == 0:
            for i in range(count1):
                star_increase += 2
            count1 += 1
            break
        while floor_height > 5 and ispremier(floor_height) == True:
            for i in range(count2):
                star_increase += 2
            count2 += 1
            break
        while floor_height > 5 and not floor_height % 3 == 0 and not ispremier(floor_height) == True:
            for i in range(count3):
                star_increase += 2
            count3 += 1
            break
        for j in range(floor_height):
            line = line_pattern[:1] + (star_number + star_increase) * "*" + line_pattern[1:]
            star_number += 2
        floor_height += 1
        star_increase += 4
    return len(line)

def floor_offset(nber_passages1 : int, nber_passages2 : int, nber_passages3 : int , floor_height : int, star_increase : int, spacing : int) -> tuple:
    while floor_height > 5 and floor_height % 3 == 0:
        for i in range(nber_passages1):
            star_increase += 2
            spacing -= 1
        nber_passages1 += 1
        break
    while floor_height > 5 and ispremier(floor_height) == True:
        for i in range(nber_passages2):
            star_increase += 2
            spacing -= 1
        nber_passages2 += 1
        break
    while floor_height > 5 and not floor_height % 3 == 0 and not ispremier(floor_height) == True:
        for i in range(nber_passages3):
            star_increase += 2
            spacing -= 1
        nber_passages3 += 1
        break
    return nber_passages1, nber_passages2, nber_passages3, star_increase, spacing

def ispremier(n : int) -> bool:
    i = 2
    while i < n and n % i != 0:
        i += 1
    if i == n:
        return True
    else:
        return False

def build_single_line(lines : list, spacing : int, line_pattern : str, star_number : int, star_increase : int) -> list:
    line = spacing * " " + line_pattern[:1] + (star_number + star_increase) * "*" + line_pattern[1:]
    lines.append(line + "\n")
    return lines

def build_last_floor(n : int, nber_passages1 : int, nber_passages2 : int, nber_passages3 : int, lines : list, spacing : int, line_pattern : str, star_number : int, star_increase : int, floor_height : int) -> None:
    door_height = n
    door_or_poignee = False
    var = floor_offset(nber_passages1, nber_passages2, nber_passages3, floor_height, star_increase, spacing)
    star_increase = var[3]
    spacing = var[4]
    if n == 1:
        for i in range(floor_height - 1):
            build_single_line(lines, spacing, line_pattern, star_number, star_increase)
            star_number += 2
            spacing -= 1
        build_single_door_line(n, lines, spacing, line_pattern, star_number, star_increase, door_or_poignee)
    else:
        for i in range(2):
            build_single_line(lines, spacing, line_pattern, star_number, star_increase)
            star_number += 2
            spacing -= 1
        for i in range(1, n + 1):
            if i == ceil(n / 2):
                if n >= 5:
                    door_or_poignee = True
            else:
                door_or_poignee = False
            build_single_door_line(n, lines, spacing, line_pattern, star_number, star_increase, door_or_poignee)
            star_number += 2
            spacing -= 1


def build_single_door_line(n : int, lines : list, spacing : int, line_pattern : str, star_number : int, star_increase : int, door_or_poignee : bool) -> list:
    if door_or_poignee == False:
        line = spacing * " " + line_pattern[:1] + door(n, star_number, star_increase) + line_pattern[1:]
        lines.append(line + "\n")
    else:
        stars_on_floor = star_number + star_increase
        if n % 2 == 0:
            n -= 1
        door_width = n
        star_remove = stars_on_floor - door_width
        line = build_poignee_line(n, star_remove, spacing, line_pattern)
        lines.append(line + "\n")
    return lines

def door(n : int, star_number : int, star_increase : int) -> str:
    stars_on_floor = star_number + star_increase
    if n == 1:
        door_width = 1
        star_remove = stars_on_floor - door_width
        door_line = (star_remove * "*")[:int(star_remove / 2)] + door_width * "|" + (star_remove * "*")[int(star_remove / 2):]
    if n == 2:
        door_width = 3
        star_remove = stars_on_floor - door_width
        door_line = (star_remove * "*")[:int(star_remove / 2)] + door_width * "|" + (star_remove * "*")[int(star_remove / 2):]
    else:
        if n % 2 == 0:
            n -= 1
        door_width = n
        star_remove = stars_on_floor - door_width
        door_line = (star_remove * "*")[:int(star_remove / 2)] + door_width * "|" + (star_remove * "*")[int(star_remove / 2):]
    return door_line

def build_poignee_line(n : int, star_remove : int, spacing : int, line_pattern : str) -> str:
    door_line = ""
    if n >= 5:
        for i in range(1, n + 1):
            if i == ceil(n / 2):
                door_line = spacing * " " + line_pattern[:1] + (star_remove * "*")[:int(star_remove / 2)] + (n - 2) * "|" + "$" + "|" + (star_remove * "*")[int(star_remove / 2):] + line_pattern[1:]
    return door_line

def tests() -> str:
    def test_build_pyramide() -> str:
        assert build_pyramide(1) == ['  /*\\\n', ' /***\\\n', '/**|**\\\n']
        return "test_build_pyramide...OK"

    def test_handle_input() -> str:
        assert handle_input("salut") == -1
        assert handle_input(0) == ""
        assert handle_input(-15) == -1
        assert handle_input(6) == 6
        assert handle_input(6.3) == 6
        return "test_handle_input...OK"

    def test_last_line_width() -> str:
        assert last_line_width(1) == 7
        assert last_line_width(5) == 71
        assert last_line_width(10) == 211
        return "test_last_line_width...OK"

    def test_floor_offset() -> str:
        assert floor_offset(1, 1, 1, 3, 20, 4) == (1, 1, 1, 20, 4)
        assert floor_offset(3, 7, 9, 6, 30, 12) == (4, 7, 9, 36, 9)
        assert floor_offset(15, 8, 2, 18, 60, 34) == (16, 8, 2, 90, 19)
        return "test_floor_offset...OK"

    def test_ispremier() -> str:
        assert ispremier(3) == True
        assert ispremier(2) == True
        assert ispremier(6) == False
        return "test_is_premier...OK"

    def test_build_single_line() -> str:
        assert build_single_line([], 2, "/\\", 5, 3) == ["  /********\\\n"]
        assert build_single_line(["  /********\\"], 4, "||", 2, 6) == ["  /********\\", "    |********|\n"]
        return "test_build_single_line...OK"

    # def test_build_last_floor() -> str:

    def test_build_single_door_line() -> str:
        assert build_single_door_line(3, [], 3, "/\\", 3, 4, False) == ['   /**|||**\\\n']
        assert build_single_door_line(6, ['   /**|||**\\'], 5, "/\\", 6, 7, True) == ['   /**|||**\\', '     /****|||$|****\\\n']
        return "test_build_single_door_line...OK"

    def test_door() -> str:
        assert door(1, 20, 12) == "***************|****************"
        assert door(2, 20, 12) == "**************|||***************"
        assert door(10, 20, 12) == "***********|||||||||************"
        assert door(20, 36, 22) == "*******************|||||||||||||||||||********************"
        return "test_door...OK"

    def test_build_poignee_line() -> str:
        assert build_poignee_line(1, 24, 52, "()") == ""
        assert build_poignee_line(2, 640, 720, "%*") == ""
        assert build_poignee_line(3, 6, 4, "/\\") == ""
        assert build_poignee_line(5, 22, 12, "/\\") == "            /***********|||$|***********\\"
        assert build_poignee_line(8, 12, -2, "()") == "(******||||||$|******)"
        assert build_poignee_line(15, 30, 4, "==") == "    =***************|||||||||||||$|***************="
        return "test_build_poignee_line...OK"

    print(test_build_pyramide())
    print(test_handle_input())
    print(test_last_line_width())
    print(test_floor_offset())
    print(test_ispremier())
    print(test_build_single_line())
    # print(test_build_last_floor())
    print(test_build_single_door_line())
    print(test_door())
    print(test_build_poignee_line())
    return ""

if MODE == "prod":
    main()
elif MODE == "test":
    print(tests())