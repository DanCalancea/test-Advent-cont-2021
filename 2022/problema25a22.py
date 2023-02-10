import sys, fileinput


def convert(sir):
    sirn = sir.copy()
    for x in range(len(sirn)):
        sirn[x] = sirn[x].replace('-', '-1')
        sirn[x] = sirn[x].replace('=', '-2')
        sirn[x] = int(sirn[x])
    return sirn


def base5(n):
    s = ""
    while n:
        s = str(n % 5) + s
        n //= 5
    ante = 0
    s2 = ''
    peste5 = False
    for x in range(len(s) - 1, -1, -1):
        newdigit = int(s[x]) + ante
        if newdigit >= 5:
            newdigit = newdigit - 5
            peste5 = True

        if newdigit <= 2:
            s2 = str(newdigit) + s2
            if peste5:
                peste5 = False
                ante = 1
            else:
                ante = 0

            continue
        elif newdigit == 3:
            s2 = '=' + s2
            ante = 1
        elif newdigit == 4:

            s2 = '-' + s2
            ante = 1

    if ante == 1:
        s2 = '1' + s2
    return s2  #


def invertsnuf(x):
    y = int(x, 5)


def snuf(sir):
    suma = 0
    lung = len(sir)
    for x in range(lung):
        suma += sir[x] * (5 ** (lung - x - 1))

    return suma


if len(sys.argv) > 1:
    fil = open(sys.argv[1])
else:
    fil = fileinput.input(files='intrari25a22.txt')

intrare = []

for line in fil:
    line = line.strip()
    intrare.append([line[x] for x in range(len(line))])

sum = 0
for i in intrare:

    sum += snuf(convert(i))

print(sum, base5(sum))

print(base5(1257))
