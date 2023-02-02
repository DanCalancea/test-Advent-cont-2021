import sys, fileinput



class Directie():
    def __init__(self, y, x, puncte):
        self.y = y
        self.x = x
        self.puncte = puncte


def locatecub(y, x):
    for i in fete:
        if (y - 1) // L_CUB == i['y'] and (x - 1) // L_CUB == i['x']:
            return i['name']


def rotesc(directie, cum):
    for i in range(4):
        if laturi[i] == directie:
            index = i
            break
    if cum == 'L':
        nou = laturi[(index + 3) % 4]
    if cum == 'R':
        nou = laturi[(index + 1) % 4]
    return nou


def rewind(a2):
    if a2 == 'left': t2 = 'right'
    if a2 == 'right': t2 = 'left'
    if a2 == 'up': t2 = 'down'
    if a2 == 'down': t2 = 'up'

    return t2


def relativ(fata1, fata2):
    for i in laturi:
        if fata2[i] == fata1['name']:
            catre = i

    return catre


def marginicub(y, x, unde):
    und = unde

    mycub = eval(locatecub(y, x))
    xincub, yincub = x - L_CUB * mycub['x'], y - L_CUB * mycub['y']
    cubvecin = eval(mycub[unde])
    catre = relativ(mycub, cubvecin)  # fata de pe cubul vecin

    if (und, catre) in (('up', 'right'), ('right', 'up'), ('left', 'down'), ('down', 'left')):
        rotate = True
        intors = True
    if (und, catre) in (('up', 'up'), ('right', 'right'), ('left', 'left'), ('down', 'down')):
        rotate = False
        intors = True
    if (und, catre) in (('up', 'left'), ('left', 'up'), ('down', 'right'), ('right', 'down')):
        rotate = True
        intors = False
    if (und, catre) in (('up', 'down'), ('down', 'up'), ('left', 'right'), ('right', 'left')):
        rotate = False
        intors = False

    if catre == 'left':
        mx = cubvecin['x'] * L_CUB
        if rotate:
            my = L_CUB * cubvecin['y'] + xincub - 1 if not intors else L_CUB * (
                    cubvecin['y'] + 1) - xincub
        else:
            my = L_CUB * cubvecin['y'] + yincub - 1 if not intors else L_CUB * (
                    cubvecin['y'] + 1) - yincub
    if catre == 'right':
        mx = (cubvecin['x'] + 1) * L_CUB - 1
        if rotate:
            my = L_CUB * cubvecin['y'] + xincub - 1 if not intors else L_CUB * (
                    cubvecin['y'] + 1) - xincub
        else:
            my = L_CUB * cubvecin['y'] + yincub - 1 if not intors else L_CUB * (
                    cubvecin['y'] + 1) - yincub
    if catre == 'up':
        my = cubvecin['y'] * L_CUB
        if rotate:
            mx = L_CUB * cubvecin['x'] + yincub - 1 if not intors else L_CUB * (
                    cubvecin['x'] + 1) - yincub
        else:
            mx = L_CUB * cubvecin['x'] + xincub - 1 if not intors else L_CUB * (
                    cubvecin['x'] + 1) - xincub

    if catre == 'down':
        my = (cubvecin['y'] + 1) * L_CUB - 1
        if rotate:
            mx = L_CUB * cubvecin['x'] + yincub - 1 if not intors else L_CUB * (
                    cubvecin['x'] + 1) - yincub
        else:
            mx = L_CUB * cubvecin['x'] + xincub - 1 if not intors else L_CUB * (
                    cubvecin['x'] + 1) - xincub
    if harta[my + 1][mx + 1] == LIBER:
        und = rewind(catre)

    return my + 1, mx + 1, und


def move(y, x, lung):
    
    global direction
    und = direction
    unde = eval(und)
    nexty, nextx = y, x
    for i in range(lung):
        if harta[nexty + unde.y][nextx + unde.x] == BLOCAT:
            return nexty, nextx
        elif harta[nexty + unde.y][nextx + unde.x] == ZID:
            yy, xx, und = marginicub(nexty, nextx, und)
            if harta[yy][xx] == LIBER:
                nexty, nextx = yy, xx
                direction = und
                unde = eval(und)
            else:
                return nexty, nextx
        else:
            nextx += unde.x
            nexty += unde.y
    return nexty, nextx


left = Directie(0, -1, 2)
right = Directie(0, 1, 0)
up = Directie(-1, 0, 3)
down = Directie(1, 0, 1)


# ------------------------------- input ----------------------------------------------


if len(sys.argv) > 1:
    fil = open(sys.argv[1])
else:
    fil = fileinput.input(files='intrari22a222.txt')

L_CUB = 50
inputnou = []
traseu = []
coloane = 0
linii = 0
LIBER, BLOCAT, ZID = 0, 7, 9

for line in fil:
    line = line.replace('\n', '')
    inputnou.append(line)
    if len(line) == 0: break
    coloane = max(coloane, len(line))
    linii += 1

nr = 0

harta = [[ZID for x in range(coloane + 2)] for y in range(linii + 2)]

print(coloane, linii)
for line in inputnou:

    print(line)
    if nr == linii: continue
    if nr >= linii + 1:
        continue
    for i in range(len(line)):

        if line[i] == '#':
            harta[nr + 1][i + 1] = BLOCAT
        elif line[i] == '.':
            harta[nr + 1][i + 1] = LIBER
    nr += 1
for line in fil:
    line = line.replace('\n', '')
    line = line.replace('R', ',R,')
    line = line.replace('L', ',L,')

    traseu.append([x for x in line.split(',')])

traseu = traseu[0]
print(traseu)

start = (1, harta[1].index(0))
print('punct de start', start)

# ------------------------------- input ----------------------------------------------


unu, doi, trei, patru, cinci, sase = dict(), dict(), dict(), dict(), dict(), dict()
fete = [unu, doi, trei, patru, cinci, sase]
fetenume = ['unu', 'doi', 'trei', 'patru', 'cinci', 'sase']

for i in fetenume:
    eval(i)['name'] = i
    eval(i)['left'] = 'nimic'
    eval(i)['right'] = 'nimic'
    eval(i)['up'] = 'nimic'
    eval(i)['down'] = 'nimic'
    eval(i)['opus'] = 'nimic'

xcub, ycub = coloane // L_CUB, linii // L_CUB
c = 0

for y in range(ycub):
    for x in range(xcub):
        if harta[y * L_CUB + 3][x * L_CUB + 3] == ZID: continue

        laturi_cub = [(y, x, y, x + 1), (y, x + 1, y + 1, x + 1), (y + 1, x, y + 1, x + 1),
                      (y, x, y + 1, x)]

        fete[c]['laturi'] = laturi_cub
        fete[c]['x'], fete[c]['y'] = x, y

        c += 1

laturi = ('up', 'right', 'down', 'left')

for i in fete:
    for j in fete:
        if i == j: continue
        for a in range(4):  # patru laturile fete
            if i['laturi'][a] in j['laturi']:
                i[laturi[a]] = j['name']
opusi = []

for i in fete:  # caut fete opuse
    for j in fete:
        if abs(i['y'] - j['y']) == 2 and abs(i['x'] - j['x']) == 0:
            opusi.append(i['name'])
            opusi.append(j['name'])
            i['opus'], j['opus'] = j['name'], i['name']

            if i['left'] == 'nimic': i['left'] = j['left']
            if i['right'] == 'nimic': i['right'] = j['right']
            if i['up'] == 'nimic':  i['up'] = j['down']
            if i['down'] == 'nimic': i['down'] = j['up']
        if abs(i['y'] - j['y']) == 0 and abs(i['x'] - j['x']) == 2:
            opusi.append(i['name'])
            opusi.append(j['name'])
            i['opus'], j['opus'] = j['name'], i['name']

            if i['left'] == 'nimic': i['left'] = j['right']
            if i['right'] == 'nimic': i['right'] = j['left']
            if i['up'] == 'nimic': i['up'] = j['up']
            if i['down'] == 'nimic': i['down'] = j['down']
        if abs(i['y'] - j['y']) == 2 and abs(i['x'] - j['x']) == 2:

            opusi.append(i['name'])
            opusi.append(j['name'])
            i['opus'], j['opus'] = j['name'], i['name']

            if i['left'] == 'nimic': i['left'] = j['right']
            if i['right'] == 'nimic': i['right'] = j['left']
            if i['up'] == 'nimic': i['up'] = j['down']
            if i['down'] == 'nimic': i['down'] = j['up']

if len(set(opusi)) == 4:
    unu1 = list(sorted(set(fetenume).difference(set(opusi))))
    a1, a2 = eval(unu1[0]), eval(unu1[1])
    a1['opus'], a2['opus'] = a2['name'], a1['name']

    if a1['left'] == 'nimic': a1['left'] = a2['up']
    if a1['right'] == 'nimic': a1['right'] = a2['down']
    if a1['up'] == 'nimic':  a1['up'] = a2['right']
    if a1['down'] == 'nimic': a1['down'] = a2['left']
    if a2['left'] == 'nimic': a2['left'] = a1['up']
    if a2['right'] == 'nimic': a2['right'] = a1['down']
    if a2['up'] == 'nimic': a2['up'] = a1['right']
    if a2['down'] == 'nimic': a2['down'] = a1['left']

for i in fete:  # rezolv

    if i['left'] == 'nimic':
        for j in fete:
            if j == i or j['name'] == i['opus']: continue
            if j['x'] == i['x'] - 1 and abs(j['y'] - i['y']) == 1:
                i['left'] = j['name']
                break
    if i['right'] == 'nimic':
        for j in fete:
            if j == i or j['name'] == i['opus']: continue
            if j['x'] == i['x'] + 1 and abs(j['y'] - i['y']) == 1:
                i['right'] = j['name']
                break
    if i['up'] == 'nimic':
        for j in fete:
            if j == i or j['name'] == i['opus']: continue
            if abs(j['x'] - i['x']) == 1 and j['y'] == i['y'] - 1:
                i['up'] = j['name']
                break
    if i['down'] == 'nimic':
        for j in fete:
            if j == i or j['name'] == i['opus']: continue
            if abs(j['x'] - i['x']) == 1 and j['y'] == i['y'] + 1:
                i['down'] = j['name']
                break

for i in fete:  # rezolv daca lipseste 1 vecin
    exvecini = []
    nealocat = []
    for z in laturi:
        if i[z] != 'nimic':
            exvecini.append(i[z])
        else:
            nealocat.append(z)
    if len(exvecini) == 3 and i['opus'] != 'nimic':
        exvecini.append(i['opus'])
        exvecini.append(i['name'])
        unu1 = set(fetenume).difference(set(exvecini))
        i[nealocat[0]] = list(unu1)[0]
print()
print('fata   left right up  down     opus ')
print('-----------------------------------')
for i in fete:
    print(i['name'], '->', i['left'], i['right'], i['up'], i['down'], '->', i['opus'])
print('-----------------------------------')
(y, x) = start
direction = 'right'
numar = True

for i in traseu:

    if numar:
        j = int(i)
        y, x = move(y, x, int(i))
    else:
        direction = rotesc(direction, i)
    numar = not numar

print('rezultat partea a 2 a', eval(direction).puncte + 1000 * y + 4 * x)
