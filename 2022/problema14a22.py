import sys, fileinput


def drop(xx,yy):
    global sol,curge,plin

    if yy>=sol :
        curge=True
        return
    x,y=xx,yy+1

    down,left, right=testpunct(x, y)
    if down:
        if  not left:
            drop(x-1, y)
        elif not right:

            drop(x+1, y)
        elif left and right:
            if yy==0:
                plin=True
                return
            zone.add((xx,yy))
            return
    else :
        drop(x, y)

def testpunct(x, y):
    down, left, right = False, False, False

    if (x , y) in zone: down = True
    if (x - 1, y) in zone: left = True
    if (x + 1, y) in zone: right = True

    return down, left, right


if len(sys.argv) > 1:
    fil = open(sys.argv[1])
else:
    fil = fileinput.input(files='intrari14a22.txt')
curge=False
plin=False
START = (500,0)
intrare = []
zone = set()
sol=0
for line in fil:
    line = line.strip()
    intrare = [x for x in line.split(' -> ')]
    for x in range(0, len(intrare) - 1):

        a, b = intrare[x].split(',')
        c, d = intrare[x + 1].split(',')
        a, c = min(a, c), max(a, c)
        b, d = min(b, d), max(b, d)
        sol=max(sol,int(d))

        for i in range(int(a), int(c)+1):
            for j in range(int(b), int(d)+1):

                zone.add((i, j))

print(sol)

partea2=True
if partea2:sol+=2
INFINIT=1000

if partea2:
    for x in range(-INFINIT, INFINIT):
        zone.add((x, sol))

count=0
mai=True
while mai:
    # if count % 100 == 0: print()
    # print('.',end='')

    drop (500,0)
    mai=not curge and not plin
    count+=1

print(plin,curge)
if partea2:
    print ('rezultat partea a 2 a',count)
else :
    print ('rezultat partea 1a ',count-1)

