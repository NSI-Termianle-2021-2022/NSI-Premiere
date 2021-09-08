import sys

def get_map_from_file(file_name: str):
    if len(file_name) < 5 or file_name[-4:] != ".map":
        return "Error : wrong file format pass"

    try:
        fo = open(file_name, "r")
    except Exception:
        return 'no file'

    cdef list my_map = []
    cdef str line = "start"
    while line:
        line = fo.readline()
        if len(line) > 0:
            my_map.append(line.strip("\n").split())
    fo.close()

    return my_map


cpdef str main():
    if '-t' in sys.argv or '--test' in sys.argv:
        return tests()
    cdef str retour = ""
    cdef dict parameters = {
        "-p": project_parameter(), "--project": project_parameter(),
        "-a": authors_parameter(), "--authors": authors_parameter(),
        "-v": verbose_parameter(), "--verbose": verbose_parameter(),
        "-h": help_parameter(), "--help": help_parameter(),
    }

    if len(sys.argv) < 2:
        return "Please enter a parameter"

    else:
        i = 1
        while i <= len(sys.argv) - 1:
            if sys.argv[i] == '-f' or sys.argv[i] == '--file':
                retour += r_or_c_or_else(sys.argv)
                i += 1
            elif sys.argv[i] in parameters:
                retour += parameters[sys.argv[i]] + '\n'
            elif sys.argv[i] == '-r' or sys.argv[i] == '--print-result' or sys.argv[i] == '-c' or sys.argv[
                i] == '--print-coordinates' or sys.argv[i] == '--with-cython' or sys.argv[i] == '-w':
                None
            else:
                retour += 'Error, parameter ' + sys.argv[i] + ' unknown\n'
            i += 1
        return retour

cdef str r_or_c_or_else(list argv):
    retour = ""
    try:
        map = get_map_from_file(argv[argv.index('-f') + 1])
    except (ValueError, IndexError):
        None
        try:
            map = get_map_from_file(argv[argv.index('--file') + 1])
        except (ValueError, IndexError):
            return 'Problem, empty file or no file'

    if '-r' in argv or '--print-result' in argv:
        solved_map = print_solved_map(map)
        for line in solved_map:
            retour += " ".join(line)+'\n'
    elif '-c' in argv or '--print-coordinates' in argv:
        square = find_carre(map)
        if square[0][0] == 0 and square[0][1] == 0:
            retour += str(((0, 0), (0, 0)))
        else:
            retour += str(((square[0][0], square[0][1]), (square[0][0] + square[1] - 1, square[0][1] + square[1] - 1))) + "\n"

    else:
        retour += 'No output mode define\n'
    return retour


cdef str project_parameter():
    return "Projet : lpgcdm-0"

cdef str authors_parameter():
    return "Samuel Placek" + "\n" + "Gabriel Gasnier"

cdef str verbose_parameter():
    return project_parameter() + "\n" + authors_parameter()

cdef str help_parameter():
    return "Pour passer en parametre le fichier de la map, il faut mettre '-f' ou '--file' et le nom du fichier .map \nAjoutez l'argument -w ou --with-cython pour lancer avec cython"

def test_parameter():
    return tests()

def find_carre(list map):
    cdef int max_square_side = 0
    cdef (int, int) first_coordinate = (0, 0)
    cdef int y = 0
    while y < len(map)-max_square_side:
        x = 0
        while x < len(map[y])-max_square_side:
            if map[y][x] == ".":
                square_side = get_square_side(map, x, y)
                if square_side > max_square_side:
                    max_square_side = square_side
                    first_coordinate = (x, y)
            x += 1
        y += 1
    return (first_coordinate, max_square_side)

cdef list print_solved_map(list map):
    cdef ((int,int), int) coordonates = find_carre(map)
    for i in range(coordonates[1]):
        for j in range(coordonates[1]):
            map[coordonates[0][1] + i][coordonates[0][0] + j] = "x"
    return map

cdef bint is_square_available(list map, int x, int y, int square_side):
    cdef (int, int) size = (len(map[0]), len(map))
    cdef list validation_tab = []
    if x + square_side > size[0] or y + square_side > size[1]:
        return False
    for i in range(square_side):
        for j in range(square_side):
            if map[y][x + j] == ".":
                if map[y + i][x + j] == ".":
                    validation_tab.append(True)
                else:
                    validation_tab.append(False)
            else:
                validation_tab.append(False)
    for k in validation_tab:
        if k == False:
            return False
    return True

cdef int get_square_side(list map,int x, int y):
    cdef int square_side = 2
    while is_square_available(map, x, y, square_side):
        square_side += 1
    if (x > len(map[0]) or y > len(map)) or map[y][x] == "o":
        square_side = 1
    return square_side - 1

def tests():
    test_get_map_from_file()
    test_project_parameter()
    test_authors_parameter()
    test_verbose_parameter()
    test_help_parameter()
    test_is_square_availabre()
    test_get_square_side()
    test_find_carre()
    test_r_or_c_or_else()
    # test_print_solved_map()
    test_r_or_c_or_else()
    return "All tests...OK"

def test_get_map_from_file() -> str:
    assert get_map_from_file("file1.txt") == "Error : wrong file format pass"
    assert get_map_from_file(".map") == "Error : wrong file format pass"
    assert get_map_from_file("truc") == "Error : wrong file format pass"
    return "test get_map_from_file...OK"

def test_project_parameter() -> str:
    assert project_parameter() == "Projet : lpgcdm-0"
    return "test project_parameter()...OK"

def test_authors_parameter() -> str:
    assert authors_parameter() == "Samuel Placek" + "\n" + "Gabriel Gasnier"
    return "test authors_parameter()...OK"

def test_verbose_parameter() -> str:
    assert verbose_parameter() == project_parameter() + "\n" + authors_parameter()
    return "test verbose_parameter()...OK"

def test_help_parameter() -> str:
    assert help_parameter() == "Pour passer en parametre le fichier de la map, il faut mettre '-f' ou '--file' et le nom du fichier .map \nAjoutez l'argument -w ou --with-cython pour lancer avec cython"
    return "test help_parameter()...OK"

def test_is_square_availabre() -> str:
    assert is_square_available(get_map_from_file('file1.map'), 6, 1, 3) == True
    assert is_square_available(get_map_from_file('file1.map'), 2, 0, 1) == True
    assert is_square_available(get_map_from_file('file1.map'), 0, 0, 4) == False
    assert is_square_available(get_map_from_file('file1.map'), 0, 0, 0) == True
    assert is_square_available(get_map_from_file('file1.map'), 56464, 5166786123, 1651465) == False
    return "test is_square_available()...OK"

def test_get_square_side() -> str:
    assert get_square_side(get_map_from_file("file1.map"), 15614, 469546) == 0
    assert get_square_side(get_map_from_file("file1.map"), 1, 0) == 0
    assert get_square_side(get_map_from_file("file2.map"), 17, 37) == 4
    return "test get_square_side...OK"

def test_find_carre() -> str:
    assert find_carre(get_map_from_file("file1.map")) == ((6, 1), 3)
    assert find_carre(get_map_from_file("file2.map")) == ((17, 37), 4)
    return "test find_carre...OK"

def test_r_or_c_or_else():
    assert r_or_c_or_else(["-f"]) == "Problem, empty file or no file"
    assert r_or_c_or_else(["-c"]) == "Problem, empty file or no file"
    assert r_or_c_or_else(["-f", "file1.map"]) == 'No output mode define\n'
    assert r_or_c_or_else(["-f", "file1.map", "-c"]) == "((6, 1), (8, 3))" + "\n"
    assert r_or_c_or_else(["-c", "-f", "file1.map"]) == "((6, 1), (8, 3))" + "\n"
    return "test r_or_c_or_else...OK"

