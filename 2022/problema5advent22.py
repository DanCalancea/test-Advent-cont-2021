import sys , fileinput

def mut (x):
    block=[]
    for j in range (-x[0]+1,1):  # aceste 2 linii se modifica 
        block.append(stive[x[1]-1][-1+j]) # ptr p1 si p2

    for j in  block:
        stive[x[2]-1].append(j)

        del(stive[x[1]-1][-1])


NUMARSTIVE=9 # se poate obtine si din prelucrarea inputului
nstop=9 # # se poate obtine si din prelucrarea inputului
sum=0
nrl=0
operatii=[]

stive=[[] for i in range (NUMARSTIVE)]



if len(sys.argv)>1:
    fil=open(sys.argv[1])
else :
    fil=fileinput.input(files='intrarip5.txt')   




for line in fil : # citim
    nrl+=1
    line = line.replace('\n', '')
    if nrl <= nstop - 1:

        for j in range(len(line)):
            if line[j] == '[':

                stive[j// 4 ].insert(0,line[j + 1])

    if nrl>=nstop+2:
        line=  line.replace('move ', '')
        line = line.replace('from ', ',')
        line = line.replace(' to ', ',')
        operatii.append([int(x) for x in line.split(',')])


for a in operatii:

    mut(a)



for i in  stive:
    print(i[-1],end='')



