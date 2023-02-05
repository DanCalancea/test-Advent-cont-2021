import sys, fileinput


class Directie():
    def __init__(self, x, y, puncte):
        self.x = x
        self.y = y
        self.puncte = puncte


def margini():
    numarelfi = 0
    xx, yy = [], []
    for y in range(l):
        for x in range(l):
            if harta[y][x] == ELF:
                xx.append(x)
                yy.append(y)
                numarelfi += 1
    c = 0
    minx, maxx = min(xx), max(xx)
    miny, maxy = min(yy), max(yy)
    for y in range(miny, maxy + 1):
        for x in range(minx, maxx + 1):
            if harta[y][x] == LIBER:
                c += 1
    return c, numarelfi


def scanez(y, x, maindirection):
    index = maindirection
    move = False
    posibil = []
    for i in unde:
        gasit = False
        und = eval(i)
        for (xmove, ymove) in und.puncte:
            if harta[y + ymove][x + xmove] == ELF:
                posibil.append(False)
                gasit = True
                break

        if not gasit: posibil.append(True)

    if False in posibil and True in posibil: move = True

    gata = False if move else True
    while not gata:
        if posibil[index]:
            gata = True
        else:
            index = (index + 1) % 4

    return move, index


def tiparesc():
    for y in range(l):
        print()
        for x in range(l):
            index = harta[y][x]
            tip = '.' if index == LIBER else '#'
            print(tip, end='')


def pas1():
    elfistatici = 0
    global maindirection
    map2 = [[NEUTRU for i in range(l + 1)] for j in range(l + 1)]

    for y in range(l):
        for x in range(l):
            if harta[y][x] != LIBER:
                move, catr = scanez(y, x, maindirection)
                if move:
                    catre = eval(unde[catr])

                    map2[y][x] = catr

                    map2[y + catre.y][x + catre.x] += 1

                else:
                    elfistatici += 1
    for y in range(l):
        for x in range(l):
            inde = map2[y][x]

            if inde < NEUTRU:

                catre = eval(unde[inde])
                if map2[y + catre.y][x + catre.x] - NEUTRU == 1:
                    harta[y][x] = LIBER
                    harta[y + catre.y][x + catre.x] = ELF
    maindirection += 1
    maindirection = maindirection % 4

    return elfistatici


# ------------------------------- input ----------------------------------------------

nord = Directie(0, -1, [(-1, -1), (0, -1), (1, -1)])
sud = Directie(0, 1, [(-1, 1), (0, 1), (+1, 1)])
est = Directie(1, 0, [(1, -1), (1, 0), (1, 1)])
vest = Directie(-1, 0, [(-1, -1), (-1, 0), (-1, 1)])

maindirection = 0
unde = ['nord', 'sud', 'vest', 'est']
NEUTRU = 9
DIMENSIUNE = 70
RELATIV = 110
l = DIMENSIUNE + RELATIV
LIBER, ELF = 7, 0
harta = [[LIBER for i in range(l + 1)] for j in range(l + 1)]
hartafilter = [[NEUTRU for i in range(l + 1)] for j in range(l + 1)]
if len(sys.argv) > 1:
    fil = open(sys.argv[1])
else:
    fil = fileinput.input(files='intrari23a222.txt')

intrari = []
count = 0
for line in fil:
    line = line.strip()

    for i in range(len(line)):
        harta[count + RELATIV // 2][i + RELATIV // 2] = LIBER if line[i] == '.' else ELF

    count = count + 1

# ------------------------------- input ----------------------------------------------

numarspatii, numarelfi = margini()

gasit = False

c = 0
while not gasit:
    c += 1
    nr = pas1()
    if nr == numarelfi:
        gasit = True
    if c == 10:
        numarspatii, numarelfi = margini()
        print()
        print('Rezultat la partea 1a', numarspatii)
        print()
        print('calculez ..')
print()
print('Rezultat la partea 2a ', c)
