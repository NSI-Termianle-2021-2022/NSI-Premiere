import leonard_loadpyramide as loadpyramide

global stock, frag, stars
frag, stars = [], -1



def createstars(e: int) -> list:
    global frag, stars

    stock = []
    length = 0
    c = 0
    size = e

    for i in range(size):
        length += 3 + c
        frag.append(length+1)
        c += 1

    for i in range(1, length+1):
        if i in frag:
            stars += 6
        else:
            stars += 2

        tmpstar = ''
        for k in range(stars):
            tmpstar += '*'

        stock.append("/" + tmpstar + "\\")

    return stock


def createdoor(e: int) -> list:
    global frag, stars
    stock = createstars(e)
    size = e

    TMPL = list()
    for i in range(1, size+1):
        TMPL.append(stock[len(stock)-i])

    mid2 = (stars + 2) // 2

    if size % 2 == 0:
        pm = (size/2)-1
    else:
        pm = size//2

    for i in range(len(TMPL)):

        sstr = ''
        lstr = list()
        for s in TMPL[i]:
            lstr.append(s)

        if size%2 == 0:
            for k in range(1, ((size-1)//2)+1):
                lstr[mid2-k] = "|"
            for k in range(1, ((size-1)//2)+1):
                lstr[mid2+k] = "|"
        else:
            for k in range(1, (size//2)+1):
                lstr[mid2-k] = "|"
            for k in range(1, (size//2)+1):
                lstr[mid2+k] = "|"

        if i == pm:
            lstr[mid2+1] = "$"

        lstr[mid2] = "|"

        mid2 -=1

        for k in lstr:
            sstr += k

        TMPL[i] = sstr

    for i in range(size+1):
        if i == 0:
            stock[len(stock)-1] = TMPL[0]
        else:
            stock[len(stock) - i] = TMPL[i - 1]


    return stock



def createspace(e: int) -> list:
    global frag, stars
    stock = createdoor(e)

    mid = (stars + 2) // 2

    frag2 = list()
    for i in frag:
        frag2.append(i-1)

    for i in range(len(stock)):
        if i in frag2:
            tmpspace = ''
            for k in range(mid-3):
                tmpspace += ' '
            mid -= 3
            stock[i] = tmpspace + stock[i]
        else:
            tmpspace = ''
            for k in range(mid - 1):
                tmpspace += ' '
            mid -= 1
            stock[i] = tmpspace + stock[i]

    return stock


def display(e: int) -> None:
    stock = createspace(e)
    for i in stock:
        print(i)
    print("\n")


while True:
    while True:
        e = input('Entrer la taille de la pyramide: ')
        print("")
        try:
            print("a")
            e = int(e)
            print("b")
            break
        except ValueError:
            print("la taille n'est pas valide !")

    if 0 < e < 6:
        l = loadpyramide.load(e)
        for s in l:
            print(str(s)+"\\")
        print('\'')

    elif e == 0:
        print('\'')
    else:
        display(e)
