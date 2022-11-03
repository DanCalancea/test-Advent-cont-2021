import sys , fileinput
from itertools import combinations_with_replacement

def mic(unu):
    if ord(unu[0]) > 96:
        return True
    else :
        return False

def vecini(alfa):
    sir=[]
    sir = puncte[alfa].split(' ')
    del (sir[-1])
    return sir

def calc(node, mici_parcurse):
    ans=0

    if node == 'end':
        return 1

    if mic(node):
        mici_parcurse.append(node)


    for vecin in vecini(node):

        if vecin not in mici_parcurse:
            mici_parcurse_nou = list(mici_parcurse)
            ans += calc(vecin,  mici_parcurse_nou)
            print('avsm',ans)

    return ans


# start program


unu=[]
intrari=[]
ans = 0
puncte=dict()



if len(sys.argv)>1:
    fil=open(sys.argv[1])
else :
    fil=fileinput.input(files='intrari12.txt')


for line in fil: #

   line=line.replace('\n','')

   intrari.append(line)



for i in intrari :
    a1 , a2= i.split('-')
    puncte[a1] = puncte.get(a1,'')+a2+" "
    puncte[a2] = puncte.get(a2,'')+a1+" "


print(puncte)


print (calc('start',['start']))
















