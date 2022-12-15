import sys, fileinput


def vecini(y, x, xstart, ystart):
    min = RELATIV - 1
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if abs(i) == abs(j):
                continue
            detestat = matrix[y][x] - matrix[y + i][x + j]

            if -30 < detestat <= 1 or (x + j == xstart and y + i == ystart):

                if calcul[y + i][x + j] <= min:
                    min = calcul[y + i][x + j]

    if min == RELATIV - 1:
        return (calcul[y][x])
    else:
        return min + 1


def calculez(xstart1, ystart1):
    global calcul
    mai = True
    calcul = [[RELATIV for x in range(len(matrix[0]))] for y in range(len(matrix))]
    while mai:
        mai = False
        for y in range(1, len(calcul) - 1):
            for x in range(1, len(calcul[0]) - 1):
                calcul[ystart1][xstart1] = 1

                unu = vecini(y, x, xstart1, ystart1)
                if calcul[y][x] != unu:
                    if not (x == xstart1 and y == ystart1):
                        mai = True

                calcul[y][x] = unu

    return calcul[ydestination][xdestination + 1]


if len(sys.argv) > 1:
    fil = open(sys.argv[1])
else:
    fil = fileinput.input(files='intrari12p22 .txt')

RELATIV = 900
first = True
matrix, calcul = [], []

for line in fil:
    line = line.strip()
    if first:
        matrix.append([RELATIV for x in range(len(line) + 2)])
        first = False
    matrix.append([RELATIV] + [ord(line[x]) for x in range(len(line))] + [RELATIV])

matrix.append([RELATIV for x in range(len(matrix[0]))])
calcul = [[RELATIV for x in range(len(matrix[0]))] for y in range(len(matrix))]
for y in range(len(matrix)):
    for x in range(len(matrix[0])):
        if matrix[y][x] == 69:
            ydestination = y
            xdestination = x
        if matrix[y][x] == 83:
            ystart = y
            xstart = x

matrix[ystart][xstart] = 97  # asci a
minimum = RELATIV

for yy in range(1, len(matrix) - 1):
    for xx in range(1, 2):
        if xx > 1 and yy > 1: continue
        if matrix[yy][xx] == 97:
            print('.', end='')

            rez = calculez(xx, yy)

            if minimum > rez:
                minimum = rez
                if minimum == 300:
                    print()
                    for c in calcul:
                        print(c)
            if xx == xstart and yy == ystart:
                print()
                print('rezultat la prima parte', calcul[ydestination][xdestination + 1])

print()
print('rezultat partea a 2 a ', minimum)
