import sys, fileinput


class Piesa():
    def __init__(self, inaltime, latime, contact, points):
        self.inaltime = inaltime
        self.latime = latime
        self.contact = contact
        self.points = points


def pattern1(yrel):
    pattern = ''

    for x in range(7):
        for y in range(15):
            if bazin[yrel + y][x] == 1:
                pattern += str(y)
                break
    return pattern


def liber(piesa, x, y):
    liber = True
    for i in range(piesa.latime):
        for j in range(piesa.inaltime):
            if piesa.points[j * piesa.latime + i] == 1:
                if bazin[y + j][x + i] == 1:
                    liber = False
                    return liber

    return liber


def landing(piesa, x, y):
    landa = False
    for i in range(len(piesa.contact)):
        if bazin[y + piesa.contact[i]][x + i] == 1:
            landa = True
            break
    return landa


def margini(piesa, x, y):
    stanga = 0
    dreapta = WIDEBAZIN - piesa.latime

    for jj in range(x - 1, -1, -1):
        if not liber(piesa, jj, y):
            stanga = max(stanga, jj + 1)
            break

    for jj in range(x + 1, WIDEBAZIN - piesa.latime + 1):

        if not liber(piesa, jj, y):
            dreapta = min(dreapta, jj - 1)
            break

    return stanga, dreapta


def afiseaza(n):
    for i in range(10, -10, -1):
        try:
            print(bazin[n - i])
        except:
            None


def updatebazin(piesa, x, y):  # umple bazinul cu piesa noua

    for i in range(piesa.latime):
        for j in range(piesa.inaltime):
            if piesa.points[j * piesa.latime + i] == 1:
                bazin[y + j][x + i] = 1


# ------------------------------- input ----------------------------------------------

if len(sys.argv) > 1:
    fil = open(sys.argv[1])
else:
    fil = fileinput.input(files='intrari17a22.txt')

move = []

for line in fil:
    line = line.strip()
    for i in range(len(line)):
        misc = -1 if line[i] == '<' else 1
        move.append(misc)

lungimeintrare = len(move)

# ------------------------------- input ----------------------------------------------


istoric = dict()

linie = Piesa(1, 4, [1, 1, 1, 1], [1, 1, 1, 1])
trefla = Piesa(3, 3, [2, 3, 2], [0, 1, 0, 1, 1, 1, 0, 1, 0], )
lintors = Piesa(3, 3, [3, 3, 3], [0, 0, 1, 0, 0, 1, 1, 1, 1], )
stalp = Piesa(4, 1, [4], [1, 1, 1, 1])
patrat = Piesa(2, 2, [2, 2], [1, 1, 1, 1])

piese = [linie, trefla, lintors, stalp, patrat]
MAXHIGH = 3
WIDEBAZIN = 7
NUMARPIESE = 5
ESTIMATBAZIN = 2000  # daca este mai mare este mai sigur, pus asa ptr timp
TOTALROCK = 1000000000000  # 2022 pentru partea 1

print(lungimeintrare)
bazin = [[0 for i in range(WIDEBAZIN)] for j in range(ESTIMATBAZIN * MAXHIGH)]
bazin.append([1 for i in range(WIDEBAZIN)])
nr = 0
bottom = len(bazin) - 1
indexmove = 0
gasitrepetare = False
bottomrelativ=0
while nr < TOTALROCK:

    xstart = 2
    ystart = bottom - 3
    piesa = piese[nr % NUMARPIESE]
    ystart -= piesa.inaltime
    landi = False
    land = False  # pozitia urmatoate blocata
    bucla = 0
    pattern = ''
    while not landi:

        if bucla % 2 == 0:

            marginestanga, marginedreapta = margini(piesa, xstart, ystart)
            xstart += move[indexmove]

            xstart = marginedreapta if xstart > marginedreapta else xstart
            xstart = marginestanga if xstart < marginestanga else xstart
            indexmove =(indexmove+1)%lungimeintrare
            # indexmove+=1
            # indexmove = 0 if indexmove == lungimeintrare else indexmove


        else:
            if not land:
                ystart += 1

        if land:
            if landing(piesa, xstart, ystart):
                landi = True

        land = landing(piesa, xstart, ystart)

        bucla += 1

    updatebazin(piesa, xstart, ystart)

    bottom = min(ystart, bottom)

    nr += 1

    pattern = str(nr % NUMARPIESE) + '.' + str(indexmove) + '.' + pattern1(bottom)

    if pattern in istoric and not gasitrepetare:
        gasitrepetare = True
        index1 = istoric[pattern][0]
        nr1 = istoric[pattern][1]
        bottomrelativ = (bottom - index1) * ((TOTALROCK - nr) // (nr - nr1))
        nr = TOTALROCK - (TOTALROCK - nr) % (nr - nr1)
    else:
        istoric[pattern] = [bottom, nr]

print('Raspuns partea 1 a / 2 a ', len(bazin) - bottom - bottomrelativ - 1)
