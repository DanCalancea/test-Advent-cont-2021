import sys, fileinput
from itertools import cycle

class Directie():
    def __init__(self, y,x,puncte):
        self.y = y
        self.x = x
        self.puncte=puncte


def margini(y,x,unde):
    mx,my=x,y
    if unde =='right':
        for i in range (coloane):
            if harta[y][i]<9:
                mx=i
                break

    elif unde=='left':
        for i in range (coloane,-1,-1):
            if harta[y][i]<ZID:
                mx=i
                break

    if unde =='down':
        for i in range (linii):
            if harta[i][x]<ZID:
                my=i
                break

    elif unde=='up':
        for i in range (linii,-1,-1):
            if harta[i][x]<ZID:
                my=i
                break

    return my,mx



def move(y,x,lung,und):
    unde=eval(und)
    nexty,nextx=y,x
    for i in range(lung):
        nextx+=unde.x
        nexty+=unde.y

        if  harta[nexty][nextx]==BLOCAT:
            nextx-=unde.x
            nexty-=unde.y
            return nexty ,nextx
        elif harta[nexty][nextx]==ZID:
            yy,xx =margini(y,x,und)
            if harta[yy][xx]==0:
                nexty,nextx=yy,xx
            else:
                nextx -= unde.x
                nexty -= unde.y
                return nexty, nextx

    return nexty, nextx
left=Directie(0,-1,2)
right=Directie(0,1,0)
up=Directie(-1,0,3)
down=Directie(1,0,1)

sensuri=[right,down,left,up]
sensuri1=['right','down','left','up']
sens=cycle(sensuri1)



# ------------------------------- input ----------------------------------------------


if len(sys.argv) > 1:
    fil = open(sys.argv[1])
else:
    fil = fileinput.input(files='intrari22a222.txt')

inputnou=[]
traseu = []
coloane=0
linii=0
LIBER,BLOCAT,ZID=0,7,9
for line in fil:
    line = line.replace('\n', '')
    inputnou.append(line)
    if len(line)==0:break
    coloane=max(coloane,len(line))
    linii+=1

nr=0

harta=[[ZID for x in range(coloane+2)] for y in range (linii+2)]


for line in inputnou:

    
    if nr==linii :continue
    if nr >=linii+1:
        #traseu.append([line[x] for x in range(len(line))])
        continue
    for i in range(len(line)):

        if line[i] == '#':
            harta[nr+1][i+1]=BLOCAT
        elif line[i] == '.' :
            harta[nr + 1][i + 1] = LIBER
    nr+=1
for line in fil :

    line = line.replace('\n', '')
    line=line.replace('R',',R,')
    line=line.replace('L',',L,')

    traseu.append([x for x in line.split(',')])

traseu=traseu[0]

start=(1,harta[1].index(0))



# ------------------------------- input ----------------------------------------------
(y,x) =start
direction=next(sens)
numar=True
for i in traseu:
    if numar :
        j=int(i)
        y,x=move(y,x,int(i),direction)
    else:
        if i =='R':
            direction=next(sens)
        else:
            next(sens)   # simulez derulare inapoi
            next(sens)
            direction = next(sens)
    numar= not  numar
    

print ('scor',eval(direction).puncte+1000*y+4*x)

