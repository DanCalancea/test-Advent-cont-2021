import sys, fileinput, math


def printsir(s):  # utilizat ptr testare
    ss = ','.join(str(i) for i in s)
    for i in range(N_imbricari + 1, 0, -1):
        ss = ss.replace(str(i * -1 * IDPAR) + ',', i * '[')
        ss = ss.replace(',' + str(i * IDPAR), i * ']')


def convert(s, x):  # convertesc parantezele in numere , nu stiu daca e mare simplificare
    for i in range(x, 0, -1):
        s = s.replace(i * '[', str(i * -1 * IDPAR) + ',')
        s = s.replace(i * ']', ',' + str(i * IDPAR))
    ss = [int(i) for i in s.split(',')]

    return ss


def explozie(s, x):  # vad daca perechea este imbricata
    suma1, suma2 = 0, 0
    for i in range(len(s)):
        if abs(int(s[i])) >= IDPAR:
            if i < x:
                suma1 += s[i]
            else:
                suma2 += s[i]

    if suma1 <= -IDPAR * (N_imbricari + 1) and suma2 >= IDPAR * (N_imbricari + 1):

        return True
    else:
        return False


def split(ss):
    for i in range(len(ss) - 1):
        if IDPAR > ss[i] >= 10:
            suma1 = int(ss[i] // 2)
            suma2 = ss[i] - suma1

            ss[i] = suma1

            if ss[i + 1] >= IDPAR:  # paranteza dreapta
                ss[i + 1] += IDPAR
            else:
                ss.insert(i + 1, IDPAR)
            ss.insert(i + 1, suma2)
            if ss[i - 1] <= -1 * IDPAR:  # paranteza stanga
                ss[i - 1] -= IDPAR
            else:
                ss.insert(i, -IDPAR)

            if steprun: input()
            return ss, True
    return ss, False


def pereche(ss, x):
    if abs(ss[x]) < IDPAR and abs(ss[x + 1]) < IDPAR:
        return True

    return False


def reduce(ss):
    stanga, dreapta = None, None

    for i in range(1, len(ss) - 1):
        if pereche(ss, i):
            if explozie(ss, i):

                for j in range(i + 2, len(ss) - 1):  # caut dreapta
                    if abs(ss[j]) < IDPAR:
                        if dreapta == None: dreapta = j

                if stanga != None: ss[stanga] += ss[i]
                if dreapta != None: ss[dreapta] += ss[i + 1]

                ss[i] = 0
                ss[i - 1] += IDPAR  # reduc sau sterg parantezele
                ss[i + 2] -= IDPAR

                if ss[i + 2] == 0: del (ss[i + 2])
                del (ss[i + 1])  # sterg elementul 2
                if ss[i - 1] == 0: del (ss[i - 1])

                if steprun: input()
                return ss, True
        else:
            stanga = i if abs(ss[i]) < IDPAR else stanga
    return ss, False


def magnitude(ss):  # am facut initial recursiv dar am crezut ca se depasete numarul de recursiuni
    global mag
    while len(ss) > 0:
        i = 1
        while i < (len(ss)):

            if pereche(ss, i):

                mag = ss[i] * 3 + ss[i + 1] * 2
                if len(ss) == 4:
                    return (mag)  # Aici  nu !!!! returneaza valoarea ,nu stiu de ce
                ss[i] = mag
                ss[i - 1] += IDPAR  # reduc sau sterg parantezele
                ss[i + 2] -= IDPAR
                if ss[i + 2] == 0: del (ss[i + 2])

                del (ss[i + 1])
                if ss[i - 1] == 0: del (ss[i - 1])
            i += 1  # sterg elementul 2


def calculez(sir1, sir2):
    sir = list(sir1)

    for i in sir2:
        sir.append(i)

    sir[0] -= IDPAR
    sir[-1] += IDPAR
    mai = True

    while mai:
        mai = False

        unu = True
        while unu:
            sir, unu = reduce(sir)

        sir, doi = split(sir)

        if unu or doi: mai = True

    return sir


# start program
IDPAR = 10000
steprun = False
intrari = []
N_imbricari = 4

if len(sys.argv) > 1:
    fil = open(sys.argv[1])
else:
    fil = fileinput.input(files='intrari18.txt')

for line in fil:  # citim
    line = line.strip()
    intrari.append(convert(line, N_imbricari + 1))

sir = list(intrari[0])  # iar egalitatea dintre siruri !!!!!!

for x in range(1, len(intrari)):
    sir = calculez(sir, intrari[x])

ix = (magnitude(sir))

print()
print(' Rezultatul la partea 1 : ', mag)
print()

maxmag = 0
x = 0
print(' Calculez')
while x < len(intrari):
    print('.', end="")
    for j in range(len(intrari)):
        if x != j:

            sir = calculez(intrari[x], intrari[j])
            ix = magnitude(sir)
            if maxmag < mag:
                maxmag = mag

    x += 1

print()
print()
print(' Rezultatul  la partea a 2 a este ', maxmag)
