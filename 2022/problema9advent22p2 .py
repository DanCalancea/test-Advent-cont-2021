import sys, fileinput


def listeaza():  # doar pentru testare
    tabla = [['.' for i in range(32)] for j in range(32)]
    for i in range(NODURI):
        tabla[ycoada[i] + 15][xcoada[i] + 15] = str(i)
        tabla[15][15] = 'S'
    for j in tabla:
        print()
        for x in range(len(j)):
            print(j[x], end='')


def move(i):

    op = i[0]
    cite = int(i[1])

    for a in range(cite):
        xcoada[0] += miscariposibile[op][0]
        ycoada[0] += miscariposibile[op][1]

        for nod in range(1, NODURI):

            if abs(xcoada[nod] - xcoada[nod - 1]) <= 1 and abs(ycoada[nod] - ycoada[nod - 1]) <= 1:
                continue
            else:
                if abs(ycoada[nod] - ycoada[nod - 1]) == 2 and abs(xcoada[nod] - xcoada[nod - 1]) == 1:
                    xcoada[nod] += (xcoada[nod - 1] - xcoada[nod])
                if abs(xcoada[nod] - xcoada[nod - 1]) == 2 and abs(ycoada[nod] - ycoada[nod - 1]) == 1:
                    ycoada[nod] += (ycoada[nod - 1] - ycoada[nod])

                ycoada[nod] += (ycoada[nod - 1] - ycoada[nod]) // 2
                xcoada[nod] += (xcoada[nod - 1] - xcoada[nod]) // 2


        if (xcoada[NODURI - 1], ycoada[NODURI - 1]) not in traseu:
            traseu.append((xcoada[NODURI - 1], ycoada[NODURI - 1]))


if len(sys.argv) > 1:
    fil = open(sys.argv[1])
else:
    fil = fileinput.input(files='intrari9p22.txt')  # 2192039569602, 3849876073

miscariposibile = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}


NODURI = 10  # pus 2 pentru rezultatul la prima parte
xcoada = [0 for x in range(NODURI)]
ycoada = [0 for x in range(NODURI)]

traseu = []
miscari = []

for line in fil:
    line = line.strip()
    miscari.append(line.split(' '))

for i in miscari:
    move(i)
    # listeaza() pentru testare

print(len(traseu))
