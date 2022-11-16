import sys, fileinput


def zero(i):
    difx, dify, difz, opx, opy, opz, dx, dy, dz = locatiescanner[i]

    for sonda in range  (len( scanner[i])):

        x=scanner[i][sonda][dx]*opx
        y=scanner[i][sonda][dy]*opy
        z=scanner[i][sonda][dz]*opz

        scanner[i][sonda]=[x+difx,y+dify,z+difz]



    return

def caut12(sc1, sc2):
    s1, s2 = scanner[sc1], scanner[sc2]
    for x1, y1, z1 in [[0, 1, 2]]:
        for x2, y2, z2 in variante:

            for ox1, oy1, oz1 in [[1, 1, 1]]:
                for ox2, oy2, oz2 in operatori:
                    dx, dy, dz = [], [], []
                    difx, dify, difz = 0, 0, 0
                    flagx,flagy,flagz=False,False,False
                    for i in s1:
                        for j in s2:
                            dx.append(1*i[x1] * ox1 - j[x2] * ox2)
                            dy.append(1*i[y1] * oy1 - j[y2] * oy2)
                            dz.append(1*i[z1] * oz1 -  j[z2] * oz2)

                    for a in dx:
                        if dx.count(a) >= 12:
                            difx = a
                            flagx=True
                            break

                    for a in dy:
                        if dy.count(a) >= 12:
                            dify = a
                            flagy=True
                            break

                    for i in dz:
                        if dz.count(i) >= 12:
                            difz = i
                            flagz=True
                            break

                    if flagx and flagy and flagz :

                        locatiescanner[sc2] = [  difx,   dify, difz , ox2 ,oy2, oz2, x2, y2, z2]



                        return True

    return False


scanner = []
locatiescanner = []
nrscan = -1
rezultate=[]

operatori = [[1, 1, 1], [-1, 1, -1], [-1, -1, 1], [1, -1, -1], [-1, 1, 1], [1, -1, 1], [1, 1, -1],[-1,-1,-1]]

variante = [[0, 1, 2], [1, 2, 0], [2, 0, 1], [1, 0, 2], [0, 2, 1], [2, 1, 0]]


if len(sys.argv) > 1:
    fil = open(sys.argv[1])
else:
    fil = fileinput.input(files='intrari19.txt')

#------------------- input------------------------------------

for line in fil:  # citim
    line = line.strip()

    if 15 > len(line) > 0:

        scanner[nrscan].append([int(x) for x in line.split(',')])

    elif len(line) > 14:
        nrscan += 1
        scanner.append([])
        locatiescanner.append([])
        rezultate.append([])

#--------------------input end-------------------------------------

locatiescanner[0] = [0, 0, 0, 1, 1, 1, 0, 1, 2]
sonde = []
gasite = [0]



#
while len(gasite) < len(scanner):
    for i in range(1, len(scanner)):
        if i not in gasite:
            for j in range(len(scanner)):
                if len(locatiescanner[j]) > 1:
                    if caut12(j, i):
                        gasite.append(i)
                        print(j, i, gasite)
                        zero(i)
                        print('transformat')
                        break


rezultate=[]
for i in scanner:
    for j in i:
        if j not in rezultate:
            rezultate.append(j)


print (locatiescanner)

print ('Rezultat la prima parte ',len(rezultate) )
max=0
for i in locatiescanner:
    for j in locatiescanner:
        alfa=abs(i[0]-j[0])+abs(i[1]-j[1])+abs(i[2]-j[2])
        if alfa >max : max=alfa

print ('Rezultat la a2a  parte ',max )
#ari=[[0, 0, 0, 1, 1, 1, 0, 1, 2], [-186, -2456, -2380, -1, 1, -1, 2, 0, 1], [-139, -3642, -2490, -1, -1, -1, 0, 2, 1], [-116, 2406, -2569, -1, -1, -1, 1, 0, 2], [1173, 1146, -2550, 1, 1, -1, 0, 2, 1], [-108, 1136, -57, -1, 1, 1, 1, 0, 2], [-2464, 3583, -2543, 1, -1, -1, 0, 1, 2], [2300, 1212, -2377, -1, 1, -1, 0, 1, 2], [1098, 3559, -3605, 1, 1, 1, 2, 0, 1], [-1351, 4756, -3766, -1, -1, 1, 0, 1, 2], [-67, 2257, -3688, -1, -1, -1, 2, 1, 0], [-104, -60, -1191, 1, -1, -1, 2, 0, 1], [1094, -1335, -2464, 1, 1, 1, 1, 2, 0], [1128, 2365, -2443, 1, 1, -1, 1, 0, 2], [-128, 2387, -1294, -1, 1, 1, 0, 2, 1], [-1331, 2414, -2418, -1, -1, 1, 2, 0, 1], [1113, -2504, -2563, 1, -1, -1, 1, 2, 0], [1047, -1190, -3745, 1, -1, 1, 1, 0, 2], [1099, -114, -2497, 1, -1, 1, 0, 2, 1], [-2556, 4, -2493, -1, 1, 1, 2, 1, 0], [-28, -99, -2459, -1, 1, -1, 1, 2, 0], [-3713, 5845, -3627, -1, -1, 1, 1, 2, 0], [1210, 1159, -1260, 1, 1, -1, 2, 1, 0], [-3740, -8, -2546, 1, -1, 1, 2, 1, 0], [-2562, -1288, -2553, 1, 1, -1, 2, 1, 0], [-2525, 4655, -3628, 1, 1, -1, 0, 2, 1], [2233, 2293, -2383, -1, -1, -1, 1, 0, 2], [-1290, 3504, -2383, -1, 1, 1, 0, 2, 1], [-55, 1183, -2527, 1, -1, 1, 1, 0, 2], [-2389, 5879, -3631, -1, 1, 1, 2, 1, 0], [1043, 2368, -3606, 1, 1, -1, 0, 2, 1], [-101, 2413, -146, -1, -1, -1, 2, 1, 0], [-1219, -79, -2541, 1, 1, -1, 0, 2, 1], [-158, -1274, -2455, -1, -1, 1, 2, 0, 1], [1199, -3727, -2439, -1, 1, -1, 0, 1, 2], [-1191, 3565, -3682, 1, 1, 1, 2, 0, 1]]

