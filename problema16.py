import sys, fileinput


def tobin(a):
    try:
        sir = bin(int(a))[2:]
        while len(sir) < 4:
            sir = '0' + sir
    except:
        sir = bin(ord(a) - 55)[2:]
        while len(sir) < 4:
            sir = '0' + sir
    return sir


def analizez(s):

    global total

    if len(s) < 11:
        return

    ver = s[0:V_LEN]
    tip = s[V_LEN:V_LEN + T_LEN]

    total += int(ver, 2)

    if tip == '100': # valori literale
        literal = ''
        caut = True

        nr = -1

        while caut:
           nr += 1
           left = V_LEN + T_LEN + LITERAL_LEN * nr
           right = left + LITERAL_LEN
           lit = s[left : right]
           literal += lit[1:]
           caut = True if lit[0] == '1' else False

        rezultate.append([int(literal, 2), len(s[:right])])

        analizez(s[right:])

    else:

        id = s[V_LEN + T_LEN]

        nrpachete = int(s[V_LEN + T_LEN + ID_LEN:V_LEN + T_LEN + ID_LEN + UNU_LEN], 2) if id == '1' else 0
        nrpachete = 2 if int(tip, 2) in [6, 7, 5] else nrpachete
        lungimepachete = int(s[V_LEN + T_LEN + ID_LEN:V_LEN + T_LEN + ID_LEN+ZERO_LEN], 2) if id == '0' else 0
        rezultate.append(['o', int(tip, 2), nrpachete, lungimepachete]) # inserez operatorii in sir

        start = V_LEN + T_LEN + ID_LEN + UNU_LEN if id == '1' else V_LEN + T_LEN + ID_LEN + ZERO_LEN

        analizez(s[start:])


def operez(op, multime):

    if op == 0:  rezultat = sum(multime)
    elif op == 1:
        rezultat = 1
        for i in multime: rezultat = rezultat * i
    elif op == 2:   rezultat = min(multime)
    elif op == 3:   rezultat = max(multime)
    elif op == 5:   rezultat = 1 if multime[0] < multime[1] else 0   #pus invers deoarece scanez de la coada
    elif op == 6:   rezultat = 1 if multime[0] > multime[1] else 0   #pus invers deoarece scanez de la coada
    elif op == 7:   rezultat = 1 if multime[0] == multime[1] else 0

    return rezultat


# start program

V_LEN, T_LEN, LITERAL_LEN, ZERO_LEN,UNU_LEN,ID_LEN = 3, 3, 5, 15,11,1

cod = ''
rezultate = []

if len(sys.argv) > 1:
    fil = open(sys.argv[1])
else:
    fil = fileinput.input(files='intrari16.txt')

for line in fil:  # citim

    line = line.strip()
    cod = ''.join(list(map(tobin, list(line))))

#--------------------------------------------------------------------------

total = 0

analizez(cod)

i = 1
while len(rezultate) > 1:
    llen = len(rezultate) - 1

    if rezultate[llen - i][0] == 'o':
        print('am gasit operand', llen)
        op, nrop, cite, lungime = rezultate[llen - i]
        if cite == 0:             # aflu numarul de pachete acolo unde nu este specificat
            ll, nugasesc, jj = 0, True, 0
            while nugasesc:
                jj += 1
                ll += rezultate[llen - i + jj][1]
                if lungime - ll == 0:
                    nugasesc = False
            cite = jj

        multim, lung = [], 0      # formez multimea de calcul pentru operand
        for j in range(cite):
            multim.append(rezultate[llen - i + cite - j][0])
            lung += rezultate[llen - i + cite - j][1]
            del (rezultate[llen - i + cite - j])

        del (rezultate[llen - i])
        lungime = lung + V_LEN + T_LEN + ID_LEN + UNU_LEN if lungime == 0 else lungime + V_LEN + T_LEN + ID_LEN + ZERO_LEN
        rezultate.insert(llen - i, [operez(nrop, multim), lungime])
        i = 1
    else:
        i += 1

print()
print('Rezultatul la prima parte este : ', total)
print('Rezultatul la partea a 2 este :' ,rezultate[0][0])
