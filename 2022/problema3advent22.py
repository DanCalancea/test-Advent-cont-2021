import sys, fileinput


def prior(a):
    if ord(a) >= 97:
        return ord(a) - 96
    else:
        return ord(a) - 38


if len(sys.argv) > 1:
    fil = open(sys.argv[1])
else:
    fil = fileinput.input(files='intrarip3.txt') 

win = {'A Y': 4, 'B X': 1, 'C Z': 7, 'A X': 2, 'B Y': 5, 'C X': 2, 'C Y': 6, 'A Z': 8, 'B Z': 9}
elfi = []

sum = 0
for line in fil:  # citim

    line = line.replace('\n', '')
    unu = line[:len(line) // 2]
    doi = line[len(line) // 2:]
    elfi.append(line)
    gasit = False
    for j in range(len(unu)):
        if doi.count(unu[j]) >= 1:
            sum += prior(unu[j])
            gasit = True
            break
suma = 0
for j in range(0, len(elfi), 3):
    for i in range(len(elfi[j])):
        if elfi[j + 1].count(elfi[j][i]) > 0 and elfi[j + 2].count(elfi[j][i]) > 0:
            suma += prior(elfi[j][i])
            break



print('rezultat partea 1:',sum)
print('rezultat partea 2:',suma)
