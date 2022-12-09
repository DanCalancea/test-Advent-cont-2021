import sys, fileinput


def cite(s, inalt):
    x = 0

    for i in range(len(s)):
        x += 1
        if s[i] >= inalt:
            break
    return (x)


def vedere(x, y):
    inalt = padure[x][y]

    xleft = [padure[i][y] for i in range(x)]
    xleft.reverse()
    xright = [padure[i][y] for i in range(x + 1, len(padure[1]))]
    yup = [padure[x][i] for i in range(y)]
    yup.reverse()
    ydown = list(padure[x][i] for i in range(y + 1, len(padure)))

    return cite(xleft, inalt) * cite(xright, inalt) * cite(yup, inalt) * cite(ydown, inalt)


if len(sys.argv) > 1:
    fil = open(sys.argv[1])
else:
    fil = fileinput.input(files='intrari8a22 .txt')

padure = []

for line in fil:
    line = line.strip()
    padure.append([int(line[x]) for x in range(len(line))])

max = 0

for x in range(1, len(padure[1]) - 1):
    for y in range(1, len(padure) - 1):

        unu = vedere(x, y)
        if unu > max: max = unu

print(max)
