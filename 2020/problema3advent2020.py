import sys , fileinput




if len(sys.argv)>1:
    fil=open(sys.argv[1])
else :
    fil=fileinput.input(files='intrari3.txt')


xy=[(1,1),(3,1),(5,1),(7,1),(1,2)]
land =[]
paroleok=0
for line in fil : # citim

    line = line.replace('\n', '')
    land.append([0 if line[x] =='.' else 1 for x in range (len(line))])


lungime=len(land[0])
sosire=len(land)-1
produs=1
for IX,IY in xy :
    startx,starty=0,0
    merg=True
    numarcopaci=0
    while merg :
        startx=(startx+IX)%lungime
        starty=starty+IY
        numarcopaci+=land[starty][startx]
        if starty== sosire :
            merg=False
            produs*=numarcopaci




print (produs)
