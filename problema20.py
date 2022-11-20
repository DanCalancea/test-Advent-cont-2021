import sys, fileinput

def summatrice(m):
    sum=0
    for j in range(2, len(m) - 2):
        for i in range(2, len(m[0]) - 2):
            sum += m[j][i]
    return sum

def optimizez(m):
    relativ = 1 if m[0][0] == 0 else 0
    m2 = [[relativ for x in range(len(m[0]) + 2)] for y in range(len(m) + 2)]

    for j in range(1, len(m) - 1):
        for i in range(1, len(m[0]) - 1):
            index = str(m[j - 1][i - 1]) + str(m[j - 1][i]) + str(m[j - 1][i + 1]) + str(m[j][i - 1]) + str(
                m[j][i]) + str(m[j][i + 1]) + str(m[j + 1][i - 1]) \
                    + str(m[j + 1][i]) + str(m[j + 1][i + 1])

            index10 = int(index, 2)
            m2[j + 1][i + 1] = 1 if cod[index10] == '#' else 0


    return m2


if len(sys.argv) > 1:
    fil = open(sys.argv[1])
else:
    fil = fileinput.input(files='intrari20.txt')
cod, matrix = "", []
maicod, first = True, True
for line in fil:  # citim
    line = line.strip()

    if len(line) == 0:
        maicod = False
        continue
    if maicod:
        cod += line
    else:

        line = '..' + line + '..'
        if first:
            matrix.append([0 for x in range(len(line))])#pentru margini
            matrix.append([0 for x in range(len(line))])# pentru calcul la infinit
            first = False
        matrix.append([(1 if line[x] == '#' else 0) for x in range(len(line))])
matrix.append([0 for x in range(len(matrix[0]))])  # pentru calcul
matrix.append([0 for x in range(len(matrix[0]))])  # pentru margini


for i in range(50):
    if i==2:
        matrice=list(matrix)
    matrix = optimizez(matrix)



print('rezultat partea a 1 a :',summatrice(matrice))
print('rezultat partea a 2 a :',summatrice(matrix))
