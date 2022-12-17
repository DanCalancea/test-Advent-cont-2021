import sys, fileinput

if len(sys.argv) > 1:
    fil = open(sys.argv[1])
else:
    fil = fileinput.input(files='intrari15a22.txt')

parsing = ['Sensor at x=', ' y=', ' closest beacon is at x=', ' y=']

intrari = []

for line in fil:
    line = line.strip()
    for i in parsing:
        line = line.replace(i, '')
    line = line.replace(':', ',')
    intrari.append([int(x) for x in line.split(',')])

be = []
for x1, y1, x2, y2 in intrari:
    be.append([x1, y1, abs(x2 - x1) + abs(y2 - y1)])

done = False

INTERVAL = 4000001
for x1, y1, disto in be:  # mergem pe presupunerea ca se afla la marginea unui romb

    dist = disto + 1

    for yrelativ in [-1, 1]:
        for xrelativ in range(-dist, dist + 1):
            x = xrelativ + x1
            y = (abs(xrelativ) - dist) * yrelativ + y1

            if 0 <= x <= INTERVAL and 0 <= y <= INTERVAL:
                gasita = True

                for xa1, ya1, dist2 in be:

                    if abs(x - xa1) + abs(y - ya1) <= dist2:
                        gasita = False
                        break

                if gasita:
                    print('am  gasit la ', x, y, 'frecventa :', x * 4000000 + y)
                    done = True
                    break
        if done: break
    if done: break
