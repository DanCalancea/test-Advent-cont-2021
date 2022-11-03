import sys , fileinput

def calc ():
    for i in range (1,101):

        distante[1][1] =0
        
        for j in range (1,101):

            distante[i][j]=matrice[i][j]+min(distante[i+1][j],distante[i-1][j],distante[i][j+1],distante[i][j-1])


# --------------start program------------------------------------

matrice=[ [9990]*102 for i in range (102)]

distante=[ [2000]*102 for i in range(102)]

# -------- citesc intrarea

if len(sys.argv)>1:
    fil=open(sys.argv[1])
else :
    fil=fileinput.input(files='intrari15.txt')   #2192039569602, 3849876073

y=1

for line in fil: # citim

    line = line.replace('\n', '')

    for x in range(1,101):
        matrice[x][y]=int(line[x-1])
    y+=1

#------------  terminat citirea


calc()

for line in distante:
    print (line)

print(distante[100][100])
