import sys, fileinput
from copy import deepcopy


class Blizard:
    def __init__(self, x, y, xm, ym):
        self.x = x
        self.y = y
        self.xm = xm
        self.ym = ym


def nextminute(t):
    libere, nextharta = [], []
    for i in hartastart:
        nextharta.append(i[:])
    for y in range(0, linii - 2):
        for x in range(0, coloane - 2):
            unu = harta[y + 1][x + 1]
            if unu != FARABLIZARD:
                semn = eval(unu)
                xx = (x + semn.x * t + semn.xm) % (semn.xm)

                yy = (y + semn.y * t + semn.ym) % (semn.ym)

                nextharta[yy + 1][xx + 1] = 1

    for y in range(0, linii - 2):
        for x in range(0, coloane - 2):
            unu = nextharta[y + 1][x + 1]
            if unu == LIBER:
                libere.append((y + 1, x + 1))

    return libere



# ------------------------------- input ----------------------------------------------
drum = []
LIBER = 0
ZID = 7
FARABLIZARD = '.'
parsing = (('^', 'u'), ('v', 'd'), ('>', 'r'), ('<', 'l'))

if len(sys.argv) > 1:
    fil = open(sys.argv[1])
else:
    fil = fileinput.input(files='intrari24a222.txt')

harta, hartastart = [], []
count = 0
for line in fil:
    line = line.strip()
    for (a, b) in parsing:
        line = line.replace(a, b)
    line = line.strip()
    harta.append([line[i] for i in range(len(line))])
    hartastart.append([ZID if line[i] == '#' else LIBER for i in range(len(line))])

    count = count + 1

# ------------------------------- input ----------------------------------------------#.######
graf=dict()
coloane = len(harta[0])
linii = len(harta)
mintimp = 10E15

d = Blizard(0, 1, coloane - 2, linii - 2)
u = Blizard(0, -1, coloane - 2, linii - 2)
l = Blizard(-1, 0, coloane - 2, linii - 2)
r = Blizard(1, 0, coloane - 2, linii - 2)

rezultat = dict()

START = (0, 1)
STOP = (linii - 2, coloane - 2)
print(STOP, START)

ESTIMAT=300

graf[(START,0)]=[((1, 1),1)]

for i in range(1,ESTIMAT+1):
    libere=nextminute(i)
    for y in range(0, linii - 2):
        for x in range(0, coloane - 2):
            opt=[]
            for (y1, x1) in ((1, 0), (0, 1),(-1, 0), (0, -1)):
                if (y+1 + y1, x +1+ x1) in libere:
                    opt.append(((y+y1+1,x + x1+1),i+1))

            if len(opt) == 0: opt = [((y + 1, x + 1),i+1)]


            graf[(y+1,x+1),i]=opt

    i+=1
    
node=(START,0)
visited=[]
queue=[]
caut=True

while caut:
    caut=False

    visited.append(node)
    
    queue.append(node)

    while queue:

        s = queue.pop(0)
        a, time = s
        if a == STOP:
            mintimp = min(mintimp, time)
            print(mintimp, y, x)
            print('----------------------')

        if time > ESTIMAT: continue

        for neighbour in graf[s]:
            if neighbour not in visited:
                visited.append((neighbour))
                queue.append((neighbour))


print(mintimp)
