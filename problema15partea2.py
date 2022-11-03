import sys , fileinput


def calc ():
    for i in range (1,501):

        distante[1][1] =0

        for j in range (1,501):

            distante[i][j]=matrice[i][j]+min(distante[i+1][j],distante[i-1][j],distante[i][j+1],distante[i][j-1])


# --------------start program------------------------------------

matrice=[ [99999]*502 for i in range (502)]

distante=[ [25000]*502 for i in range(502)]

# -------- citesc intrarea

if len(sys.argv)>1:
    fil=open(sys.argv[1])
else :
    fil=fileinput.input(files='intrari15.txt')

y=1

for line in fil: # citim

    line = line.replace('\n', '')
  
    for x in range(1,101):
       
        matrice[x][y]=int(line[x-1])
    y+=1


#------------  terminat citirea
#-------------------fac matricea noua ------------------------
for x in range(5):
    for y in range(5):
        for xx in range(1,101):
            for yy in range(1,101):
                matrice[x*100+xx][y*100+yy]=matrice[xx][yy]+x+y if matrice[xx][yy]+x+y <10 else (matrice[xx][yy]+x+y)%10 +1

end=distante[500][500]
mai=True

while mai:
    calc()
    if distante[500][500]== end:
        mai=False
    else:
        end = distante[500][500]
        print(end)

print ()
print(distante[500][500])
