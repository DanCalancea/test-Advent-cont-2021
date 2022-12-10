import sys, fileinput

if len(sys.argv) > 1:
    fil = open(sys.argv[1])
else:
    fil = fileinput.input(files='intrari10p22.txt')

punctecontrol = [20, 60, 100, 140, 180, 220]
operatii = [(0, 1, 'noop', 0), (1, 1, 'noop', 0)]

contor = 0
suma = 1
for line in fil:
    contor += 2
    line = line.strip()
    if line[0] == 'n':
        line += ' 0'
        contor -= 1

    op, nr = line.split()
    suma += int(nr)
    operatii.append([contor, suma, op, int(nr)])

sum = 0

for i in punctecontrol:
    for j in range(len(operatii)):
        if operatii[j][0] >= i:
            sum += i * operatii[j - 1][1]
            break

print('rezultat partea 1 :', sum)

for y in range(6):
    print()
    for x in range(40):
        for j in range(len(operatii)):
            if operatii[j][0] >= x + y * 40 + 1:
                print
                mark = operatii[j - 1][1]
                break

        pixel = "#" if (mark - 1 <= x <= mark + 1) else ','
        if (x + 1) % 5 == 0:
            pixel = pixel + ' '
        print(pixel, end='')

print()
