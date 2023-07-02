import sys , fileinput




if len(sys.argv)>1:
    fil=open(sys.argv[1])
else :
    fil=fileinput.input(files='intrari2.txt')


numere =[]
paroleok=0
for line in fil : # citim
    cite=0
    line = line.replace('\n', '')
    line = line.replace(':', ' ')
    line = line.replace('-', ' ')
    numere=[x for x in line.split()]
    x,y,litera,parola=int(numere[0]),int(numere[1]),numere[2],numere[3]
    print(numere)
    if parola[x-1]==litera :cite+=1
    if parola[y -1] == litera: cite += 1
    if cite==1 : paroleok+=1





print (paroleok)







