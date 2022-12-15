import sys, fileinput

if len(sys.argv) > 1:
    fil = open(sys.argv[1])
else:
    fil = fileinput.input(files='intrari13a22.txt')


def compara(unu, doi):
    global raspuns

    interval = max(len(unu), len(doi))

    for i in range(interval):
        if i >= len(unu):
            raspuns = True
            return
        if i >= len(doi):
            raspuns = False
            return
        raspuns = None
        if type(unu[i]) == int and type(doi[i]) == list:
            compara([unu[i]], doi[i])

        if type(unu[i]) == list and type(doi[i]) == int:
            compara(unu[i], [doi[i]])

        if type(unu[i]) == list and type(doi[i]) == list: compara(unu[i], doi[i])
        if type(unu[i]) == int and type(doi[i]) == int:

            if unu[i] > doi[i]:

                raspuns = False
                return
            elif unu[i] < doi[i]:
                raspuns = True
                return

        if raspuns != None:
            return raspuns

    return


intrari = []

count = 0
for line in fil:
    line = line.strip()
    if len(line) > 0:
        count += 1
        lung = len(line)
        intrari.append(eval(line))

corecte = []

for x in range(0, len(intrari), 2):
    raspuns = None

    compara(intrari[x], intrari[x + 1])

    if raspuns: corecte.append(x // 2 + 1)

print('Raspuns partea 1', sum(corecte))

intrari.append([[2]])
intrari.append([[6]])
mai = True

while mai:
    mai = False

    for x in range(len(intrari) - 1):
        raspuns = None
        compara(intrari[x], intrari[x + 1])
        if not raspuns:
            intrari[x], intrari[x + 1] = intrari[x + 1], intrari[x]
            mai = True
indice = 1
for x in range(len(intrari)):

    if intrari[x] == [[2]] or intrari[x] == [[6]]:
        print('indice', x + 1)
        indice *= (x + 1)

print('Raspuns partea a 2a ', indice)
