import sys, fileinput


def roata(xx):
    global lung
    aa = pattern[xx]
    a = pattern[xx][0]
    x = intrari.index(aa)
    if a == 0:
        return
    intrari.pop(x)
    nextp = (x + a + lung - 1) % (lung - 1)
    # if nextp == 6: nextp = 0      teoretic asa este corect dar nu da rezultatul pe exemplul mare
    # elif nextp== 0: nextp =6
    intrari.insert(nextp, aa)


# ------------------------------- input ----------------------------------------------

KEY = 811589153 # 1 pentru partea 1 a
REPEAT = 10     # 1 pentru partea 1 a
if len(sys.argv) > 1:
    fil = open(sys.argv[1])
else:
    fil = fileinput.input(files='intrari20a222.txt')

intrari = []
nr = 0
for line in fil:
    line = line.strip()

    intrari.append((int(line) * KEY, nr))
    if int(line) == 0: zero = (0, nr)

    nr += 1

# ------------------------------- input ----------------------------------------------
lung = len(intrari)

key = 811589153

pattern = intrari.copy()

suma = 0
for i in range(lung * REPEAT):
    ii = i % lung
    roata(ii)

afterzero = intrari.index(zero)

for TEST in (1000, 2000, 3000):
    afterzero1 = (afterzero + TEST) % lung

    suma += intrari[afterzero1][0]

print(suma)
