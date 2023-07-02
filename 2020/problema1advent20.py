import sys , fileinput




if len(sys.argv)>1:
    fil=open(sys.argv[1])
else :
    fil=fileinput.input(files='intrari1.txt')


numere =[]

for line in fil : # citim

    line = line.replace('\n', '')
    numere.append(int(line))


for i in range (len(numere)) :
    for j in range (i+1,len(numere)):
        for k in range(j + 1, len(numere)):
            if numere[i]+ numere[j]+numere[k]== 2020 :
                print (numere[i]*numere[j]*numere[k])
                break



print (numere)




