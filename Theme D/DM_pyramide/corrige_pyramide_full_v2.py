import sys
from math import floor

# Colors
GREEN = "\033[92m"
ENDC = "\033[0m"

##################################################
#                                                #
#                     CONFIG                     #
#                                                #
##################################################

MODE = "prod"  # change to "test" to run test

# This can be modified to change the aspect of the pyramid
CHARSET = {
    "space": " ",
    "line_start": "/",
    "line_end": "\\",
    "star": "*",
    "door": "|",
    "doorknob": "$",
}

"""
Lexicon:

    - The "order" of the pyramid is its position in the series of pyramids given
      in the subject. It should match the number passed as a parameter.
    - A "line" is a series of ASCII character ended by a "newline" character.
    - An "offset" is an added line growth between two following lines.
    - A "block" is a series of following lines without offset.
    - The "last block" of the pyramid is the one at the bottom.
    - The "bottom width" of the pyramid is the width of the last printed line.
"""


##################################################
#                                                #
#                     CODE                       #
#                                                #
##################################################


def get_pyramid_height(order: int) -> int:
    """Returns the full height of the pyramid.

    This is a slight alteration of the classic "(n * (n + 1)) / 2" formula.
    """
    if order <= 0:
        return -1
    return int((order + 3) * (order + 2) / 2) - 3


def get_bottom_width(order: int) -> int:
    """Returns the bottom width of the pyramid.

    It's made of three parts:
      - the basic width
      - the normal growth of the pyramid
      - the block growth (sum of all block offsets). Block offsets are
        themselves growing :)
    """
    if order <= 0:
        return -1
    # 1. Beginning and final slash + the star in the middle
    base_width = 3

    # 2. Normal growth
    normal_growth = (get_pyramid_height(order) - 1)

    # 3. Block offset growth
    block_offsets = 0
    offset = 2

    for block in range(order - 1):
        if block > 1 and (block + 1) % 3 == 0:
            offset += 1
        block_offsets += offset

    return base_width + (normal_growth + block_offsets) * 2


def build_door_line(door_width: int, has_doorknob: bool) -> str:
    """Builds the entire door line, including the potential doorknob."""
    if door_width == 0:
        return CHARSET["star"]
    elif door_width < 3:
        return CHARSET["door"] * door_width

    door = (door_width - 2) * CHARSET["door"]
    if has_doorknob:
        door += CHARSET["doorknob"]
    else:
        door += CHARSET["door"]
    door += CHARSET["door"]
    return door


def get_door_width(order: int, block: int, block_line: int) -> int:
    """Doors' width grow every three orders, starting at 1.

    The door is printed:
      - for the last block only,
      - for all lines except the fist two.

    If there is no door for the line, the width is set to 0.
    """
    if block == order - 1 and block_line > 1:
        door_width = 2 * ((order + 1) // 3) + 1
    else:
        door_width = 0
    return door_width


def build_line(
    beginning_spaces: int,
    star_count: int,
    door_width: int,
    has_doorknob: bool,
) -> str:
    """Builds the full line without trailing newline.

    The number of stars is made of :
      - the starting star count
      - the sum of "normal" growing
      - the sum of block offsets
    """

    line = (
        beginning_spaces * CHARSET["space"]
        + CHARSET["line_start"]
        + int(star_count / 2 - door_width / 2) * CHARSET["star"]
        + build_door_line(door_width, has_doorknob)
        + int(star_count / 2 - door_width / 2) * CHARSET["star"]
        + CHARSET["line_end"]
    )
    return line


def should_have_doorknob(block: int, block_line: int) -> bool:
    if block < 4:
        return False
    return (block_line - 2) == (block // 2)


def get_block_offset(block: int) -> int:
    block_offset = 2
    for b in range(block):
        if (b - 1) % 3 == 0:
            block_offset += 1
    return block_offset


def get_beginning_spaces(order: int) -> int:
    if order <= 0:
        return -1
    return floor(get_bottom_width(order) / 2) - 1


def build_pyramid(order: int) -> str:
    """This is the main part of the program. It returns (but doesn't print) the
    pyramid of a given order.

    It returns a string with a final endline character (\n).
    """
    if order == 0:
        return ""

    pyramid = []  # We first store the pyramid as a list of strings

    block_height = 3
    star_count = 1
    beginning_spaces = get_beginning_spaces(order)

    for block in range(order):
        for block_line in range(block_height):

            door_width = get_door_width(order, block, block_line)
            has_doorknob = should_have_doorknob(block, block_line)
            line = build_line(beginning_spaces, star_count, door_width, has_doorknob)
            pyramid.append(line)
            star_count += 2  # standard line increase
            beginning_spaces -= 1

        block_height += 1
        block_offset = get_block_offset(block)
        star_count += 2 * block_offset
        beginning_spaces -= block_offset

    # We transform a list of strings into a big string with newlines inbetween
    return "\n".join(pyramid) + "\n"  # Don't forget the final "\n"!


def print_pyramid(pyramid: str) -> None:
    """This function only prints the pyramid passed as a parameter.

    Therefore it is untestable, by design.
    """
    print(pyramid, end="")


def get_order_from_input(input: str) -> int:
    """This function returns -1 in case of any error."""
    try:
        order = int(input)
    except:
        return -1
    else:
        if order < 0:
            return -1
        return order


def main() -> None:
    """The main() function calls high-level functions only.

    It handles:
      - handles the "no parameter passed" case,
      - calls the input processing,
      - handles the "negative integer passed" case,
      - calls the pyramid building,
      - launches the printing of the pyramid.
    """
    if len(sys.argv) > 1:
        order = get_order_from_input(sys.argv[1])
        if order == -1:
            print(
                f"Entrée incorrecte: {sys.argv[1]}. Vous devez saisir un entier positif ou nul"
            )
        else:
            pyramid = build_pyramid(order)
            print_pyramid(pyramid)
    else:
        print("Vous devez passer un nombre en paramètre")


##################################################
#                                                #
#                     TESTS                      #
#                                                #
##################################################


def test_get_order_from_input():
    assert get_order_from_input("") == -1
    assert get_order_from_input("2") == 2
    assert get_order_from_input("17") == 17
    assert get_order_from_input("[]") == -1
    assert get_order_from_input("-2") == -1
    assert get_order_from_input("3.5") == -1

    print(f"Test: {'get_order_from_input'.ljust(25)} - {GREEN}OK{ENDC}")


def test_get_pyramid_height():
    assert get_pyramid_height(0) == -1
    assert get_pyramid_height(1) == 3
    assert get_pyramid_height(2) == 7
    assert get_pyramid_height(3) == 12
    assert get_pyramid_height(4) == 18
    assert get_pyramid_height(5) == 25
    assert get_pyramid_height(6) == 33
    assert get_pyramid_height(7) == 42
    assert get_pyramid_height(8) == 52
    assert get_pyramid_height(13) == 117
    assert get_pyramid_height(88) == 4092

    print(f"Test: {'get_pyramid_height'.ljust(25)} - {GREEN}OK{ENDC}")


def test_get_bottom_width():
    assert get_bottom_width(0) == -1
    assert get_bottom_width(1) == 7
    assert get_bottom_width(2) == 19
    assert get_bottom_width(3) == 33
    assert get_bottom_width(4) == 51
    assert get_bottom_width(5) == 71

    print(f"Test: {'get_bottom_width'.ljust(25)} - {GREEN}OK{ENDC}")


def test_should_have_doorknob():
    assert should_have_doorknob(1, 0) == False
    assert should_have_doorknob(2, 0) == False
    assert should_have_doorknob(3, 0) == False
    assert should_have_doorknob(4, 0) == False

    assert should_have_doorknob(4, 0) == False
    assert should_have_doorknob(4, 1) == False
    assert should_have_doorknob(4, 2) == False
    assert should_have_doorknob(4, 3) == False
    assert should_have_doorknob(4, 4) == True
    assert should_have_doorknob(4, 5) == False
    assert should_have_doorknob(4, 6) == False

    assert should_have_doorknob(5, 0) == False
    assert should_have_doorknob(5, 1) == False
    assert should_have_doorknob(5, 2) == False
    assert should_have_doorknob(5, 3) == False
    assert should_have_doorknob(5, 4) == True
    assert should_have_doorknob(5, 5) == False
    assert should_have_doorknob(5, 6) == False
    assert should_have_doorknob(5, 7) == False

    print(f"Test: {'should_have_doorknob'.ljust(25)} - {GREEN}OK{ENDC}")


def test_build_door_line():
    # Without dooknob
    assert build_door_line(0, False) == "*"
    assert build_door_line(1, False) == "|"
    assert build_door_line(2, False) == "||"
    assert build_door_line(3, False) == "|||"
    assert build_door_line(4, False) == "||||"
    assert build_door_line(5, False) == "|||||"
    assert build_door_line(17, False) == "|||||||||||||||||"

    # With dooknob
    assert build_door_line(0, True) == "*"
    assert build_door_line(1, True) == "|"
    assert build_door_line(2, True) == "||"
    assert build_door_line(3, True) == "|$|"
    assert build_door_line(4, True) == "||$|"
    assert build_door_line(5, True) == "|||$|"
    assert build_door_line(6, True) == "||||$|"
    assert build_door_line(7, True) == "|||||$|"
    assert build_door_line(8, True) == "||||||$|"
    assert build_door_line(9, True) == "|||||||$|"

    print(f"Test: {'build_door_line'.ljust(25)} - {GREEN}OK{ENDC}")


def test_get_door_width():
    # Should print
    assert get_door_width(0, 0, 0) == 0
    assert get_door_width(1, 0, 2) == 1
    assert get_door_width(2, 1, 2) == 3
    assert get_door_width(3, 2, 2) == 3
    assert get_door_width(4, 3, 2) == 3
    assert get_door_width(5, 4, 2) == 5
    assert get_door_width(6, 5, 2) == 5
    assert get_door_width(7, 6, 2) == 5
    assert get_door_width(8, 7, 2) == 7
    assert get_door_width(9, 8, 2) == 7
    assert get_door_width(10, 9, 2) == 7

    # Shouldn't print
    assert get_door_width(5, 1, 2) == 0  # Not the last block
    assert get_door_width(5, 2, 2) == 0  # Not the last block
    assert get_door_width(5, 3, 2) == 0  # Not the last block
    assert get_door_width(17, 16, 1) == 0  # Not the last block
    assert get_door_width(5, 4, 0) == 0  # Last block, but first line
    assert get_door_width(5, 4, 1) == 0  # Last block, but second line

    print(f"Test: {'get_door_width'.ljust(25)} - {GREEN}OK{ENDC}")


def test_build_line():
    # Without dooknob only
    assert build_line(0, 13, 0, False) == "/*************\\"
    assert build_line(2, 1, 0, False) == "  /*\\"
    assert build_line(5, 7, 0, False) == "     /*******\\"

    print(f"Test: {'build_line'.ljust(25)} - {GREEN}OK{ENDC}")


def test_get_block_offset():
    assert get_block_offset(1) == 2
    assert get_block_offset(2) == 3
    assert get_block_offset(3) == 3
    assert get_block_offset(4) == 3
    assert get_block_offset(5) == 4
    assert get_block_offset(6) == 4
    assert get_block_offset(7) == 4
    assert get_block_offset(8) == 5
    assert get_block_offset(9) == 5
    assert get_block_offset(10) == 5
    assert get_block_offset(53) == 20
    assert get_block_offset(1631) == 546

    print(f"Test: {'test_block_offset'.ljust(25)} - {GREEN}OK{ENDC}")


def test_get_beginning_spaces():
    assert get_beginning_spaces(0) == -1
    assert get_beginning_spaces(1) == 2
    assert get_beginning_spaces(2) == 8
    assert get_beginning_spaces(3) == 15
    assert get_beginning_spaces(4) == 24
    assert get_beginning_spaces(5) == 34
    assert get_beginning_spaces(6) == 45

    print(f"Test: {'test_get_beginning_spaces'.ljust(25)} - {GREEN}OK{ENDC}")


def test_build_pyramid():
    assert build_pyramid(0) == ""
    assert (
        build_pyramid(1)
        == """  /*\\
 /***\\
/**|**\\
"""
    )
    assert (
        build_pyramid(2)
        == """        /*\\
       /***\\
      /*****\\
   /***********\\
  /*************\\
 /******|||******\\
/*******|||*******\\
"""
    )
    assert (
        build_pyramid(3)
        == """               /*\\
              /***\\
             /*****\\
          /***********\\
         /*************\\
        /***************\\
       /*****************\\
    /***********************\\
   /*************************\\
  /************|||************\\
 /*************|||*************\\
/**************|||**************\\
"""
    )
    assert (
        build_pyramid(4)
        == """                        /*\\
                       /***\\
                      /*****\\
                   /***********\\
                  /*************\\
                 /***************\\
                /*****************\\
             /***********************\\
            /*************************\\
           /***************************\\
          /*****************************\\
         /*******************************\\
     /***************************************\\
    /*****************************************\\
   /********************|||********************\\
  /*********************|||*********************\\
 /**********************|||**********************\\
/***********************|||***********************\\
"""
    )
    assert (
        build_pyramid(5)
        == """                                  /*\\
                                 /***\\
                                /*****\\
                             /***********\\
                            /*************\\
                           /***************\\
                          /*****************\\
                       /***********************\\
                      /*************************\\
                     /***************************\\
                    /*****************************\\
                   /*******************************\\
               /***************************************\\
              /*****************************************\\
             /*******************************************\\
            /*********************************************\\
           /***********************************************\\
          /*************************************************\\
      /*********************************************************\\
     /***********************************************************\\
    /****************************|||||****************************\\
   /*****************************|||||*****************************\\
  /******************************|||$|******************************\\
 /*******************************|||||*******************************\\
/********************************|||||********************************\\
"""
    )

    print(f"Test: {'build_pyramid'.ljust(25)} - {GREEN}OK{ENDC}")


def launch_tests():
    test_get_pyramid_height()
    test_get_bottom_width()
    test_should_have_doorknob()
    test_build_door_line()
    test_get_door_width()
    test_build_line()
    test_get_block_offset()
    test_get_beginning_spaces()
    test_build_pyramid()

    print("-" * 37)
    print(f"All tests {GREEN}OK{ENDC}")


if __name__ == "__main__":
    # Tests can always be launched with "> python file.py 3 test"
    if MODE == "test" or (len(sys.argv) > 2 and sys.argv[2].upper() == "TEST"):
        launch_tests()
    elif MODE == "prod":
        main()
    else:
        print("Unrecognized mode")
