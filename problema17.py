import sys , fileinput


def move(vx,vy):

    max=None
    merge,x,y=True,0,0
    firstzero=True

    while merge :
        x,y=x+vx,y+vy

        if max==None or y>max :
            max = y
        vy = vy-1
        if firstzero and vy==-1:
            firstzero=False
            vy=0

        vx = vx -1 if vx>0 else 0

        if x1<=x<=x2 and y1<=y<=y2:
            target=True
            return target , max
        if x> x2 or y< y1 :
            target=False
            return target,max

# start program

operatori=['\n','target area: ','x=',' y=']

if len(sys.argv)>1:
    fil=open(sys.argv[1])
else :
    fil=fileinput.input(files='intrari17.txt')



for line in fil: # citim

    for i in operatori:
        line=line.replace(i,'')

line=line.replace('..',',')

x1,x2,y1,y2=[int(i) for i in line.split(',')]


print ('Input : :', x1,x2,y1,y2)
print()


max,nr=0,0

for i in range (1,x2+1):    # ciclurile se pot optimiza cu formule dar nu e cazul
    for j in range(y1,(y1+y2-1)*-1):
        bun, h = move(i, j)
        if bun:
            nr += 1
            if max < h:
                max = h




print ('Rezultat la prima parte :', max , ', rezultat la partea a 2 a :',nr)
