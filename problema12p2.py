import sys , fileinput

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

def calc(node, mici_parcurse,bine,dublu):
    ans=0

    if node == 'end':
        return 1

    if mic(node):
        mici_parcurse.append(node)
        print (mici_parcurse)
        if node==dublu and bine:
            del(mici_parcurse[-1])

            bine=False


    for vecin in vecini(node):

        if vecin not in mici_parcurse:
            mici_parcurse_nou = list(mici_parcurse) # mare batai de cap mi a dat aici
            binenou = True   if bine else False #  suflu si in iaurt :) :)
            ans += calc(vecin,  mici_parcurse_nou,binenou,dublu)
            # print('avsm',ans)

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

mici=[]

for i in intrari :
    a1 , a2= i.split('-')
    puncte[a1] = puncte.get(a1,'')+a2+" "
    puncte[a2] = puncte.get(a2,'')+a1+" "
    if mic(a1) and a1 not in {'start','end'} and a1 not in mici:
        mici.append(a1)
    if mic(a2) and a2 not in {'start', 'end'} and a2 not in mici:
        mici.append(a2)


bine=True
normal=calc('start',[],True,'ubu') # numarul de variante normal
total=normal

for i in mici:
    total+=calc('start',[],True,i)
    total-=normal

print (total)














