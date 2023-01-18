import sys, fileinput
from itertools import combinations

def distanta(a, b, dist, sir):
    global d

    if a == b:
        return dist
    sirnou = sir.copy()

    distnou = dist + 1
    for valve in valvesens[a]:

        if valve == b:
            d = min(d,distnou)     
        if [valve, b] not in sirnou:
            sirnou.append([valve, b])
            distanta(valve, b, distnou, sirnou)


def cauta(start, debit, time, valvedeschise):

    global  d,maxd,variantedebit
    # if time<=30:
    #     maxd=max(maxd,debit)

    variantedebit.append([debit, time, valvedeschise])



    for valve in totalvalve: #totalvalve este totatul valvelor care au debit >0
        debitnou = debit
        valvedeschisenou = valvedeschise.copy()
        timenou = time
        startnou = valve
        if valve not in valvedeschise:
            d=1000
            try:
                d = calculdistante[start + " " + valve]  # memorizare pentru calcul rapid
            except:
                distanta(start, valve, 0, [])  # returneaza valoarea globala d
                calculdistante[start + " " + valve] = d
               # calculdistante[valve + " " + start] = d

            timenou += d + TIMPDESCHIDEREVALVA
            if timenou >= TOTALTIME-1:
                continue


            debitnou = debitnou + valvedebit[valve] * (30 - timenou)
            valvedeschisenou.append(valve)

            cauta(startnou, debitnou, timenou, valvedeschisenou)
    return

parsing = [' has flow rate=', '; tunnels lead to valves', '; tunnel leads to valve ']

if len(sys.argv) > 1:
    fil = open(sys.argv[1])
else:
    fil = fileinput.input(files='intrari16mic.txt')

d = 1000
maxd=0
TIMPDESCHIDEREVALVA=1
valvedebit, valvesens = {}, {}
variantedebit = []
calculdistante = {}
TOTALTIME=24

for line in fil:
    line = line.strip()
    for i in parsing:
        line = line.replace(i, ',')
    line = line.replace('Valve ', '')
    newline = [x.strip() for x in line.split(',')]
    valvedebit[newline[0]] = int(newline[1])
    valvesens[newline[0]] = newline[2:]


totalvalve = [] # valve cu debit diferit de 0

for x, y in valvedebit.items():
    if y > 0:
        print(x, y)
        totalvalve.append(x)
print (totalvalve)

cauta('AA', 0, 0, [])
print('Raspuns prima parte',sorted(variantedebit)[-1][0])

