import sys, fileinput

# ------------------------------- input ----------------------------------------------


if len(sys.argv) > 1:
    fil = open(sys.argv[1])
else:
    fil = fileinput.input(files='intrari21a222.txt')

monkeyready = dict()
monkey = {}
intrari = []
nr = 0
for line in fil:
    line = line.strip()
    a, b = line.split(':')
    b = b.strip()
    try:
        x = int(b)
        monkeyready[a] = x
    except:
        u1 = b[0:4]
        u2 = b[4:6].strip()
        u3 = b[7:11]
        monkey[a] = (u1, u3, u2)

# ------------------------------- input ----------------------------------------------

(u1, u2, op) = monkey['root']
monkey['root'] = (u1, u2, '-')
mai = True
copie1 = monkey.copy()
copie2 = monkeyready.copy()
start = 0
marja = 100000000000
while mai:
    monkey = copie1.copy()
    monkeyready = copie2.copy()
    monkeyready['humn'] = start

    while 'root' not in monkeyready:
        removelist = []
        for key, (u1, u2, operator) in monkey.items():
            if isinstance(u1, str) and u1 in monkeyready: u1 = monkeyready[u1]
            if isinstance(u2, str) and u2 in monkeyready: u2 = monkeyready[u2]
            if not isinstance(u1, str) and not isinstance(u2, str):
                rezultat = eval(str(u1) + operator + str(u2))
                monkeyready[key] = rezultat
                removelist.append(key)

        for x in removelist:
            del monkey[x]
    if monkeyready['root'] == 0: mai = False
    if monkeyready['root'] < 0:
        start -= marja
        marja = marja // 10
    else:
        start += marja

print(start - 1, monkeyready['root'])
