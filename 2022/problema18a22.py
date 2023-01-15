import sys, fileinput


def veciniliberi(x, y, z): # verificam daca cubul are vecini liberi

    for (i, j, k) in [(-1, 0, 0), (1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
        if ([x + i, y + j, z + k] not in cuburi) and ([x + i, y + j, z + k] not in cuburinterior):
            return True
    return False


def liber(x, y, z):  # algoritm oribil ,dar lasam asa ,verificam daca cubul este liber sa evadeze
    liberx = True
    for i in range(RELATIV):
        if [x + i, y, z] in cuburi:
            liberx = False
    if liberx: return True
    liberx2 = True
    for i in range(0, -RELATIV, -1):
        if [x + i, y, z] in cuburi:
            liberx2 = False
    if liberx2: return True
    libery = True
    for i in range(RELATIV):
        if [x, y + i, z] in cuburi:
            libery = False
    if libery: return True
    libery2 = True
    for i in range(0, -RELATIV, -1):
        if [x, y + i, z] in cuburi:
            libery2 = False
    if libery2: return True
    liberz = True
    for i in range(RELATIV):
        if [x, y, z + i] in cuburi:
            liberz = False
    if liberz: return True
    liberz2 = True
    for i in range(0, -RELATIV, -1):
        if [x, y, z + i] in cuburi:
            liberz2 = False
    if liberz2: return True

    return False


# ------------------------------- input ----------------------------------------------

if len(sys.argv) > 1:
    fil = open(sys.argv[1])
else:
    fil = fileinput.input(files='intrari18a22.txt')

cuburi = []

for line in fil:
    line = line.strip()
    cuburi.append([int(x) for x in line.split(',')])
# ------------------------------- input ----------------------------------------------


vulcan = set()
dubluri = set()
RELATIV = 15
fetecub = [[(0, 0, 0), (0, 0, 1), (1, 0, 1), (1, 0, 0)], [(0, 0, 0), (0, 0, 1), (0, 1, 1), (0, 1, 0)],
           [(0, 0, 0), (0, 1, 0), (1, 1, 0), (1, 0, 0)]
    , [(0, 0, 1), (1, 0, 1), (1, 1, 1), (0, 1, 1)], [(0, 1, 0), (0, 1, 1), (1, 1, 1), (1, 1, 0)],
           [(1, 0, 1), (1, 1, 1), (1, 1, 0), (1, 0, 0)]]

minx = min(a[0] for a in cuburi)
maxx = max(a[0] for a in cuburi)
miny = min(a[1] for a in cuburi)
maxy = max(a[1] for a in cuburi)
minz = min(a[2] for a in cuburi)
maxz = max(a[2] for a in cuburi)

for x, y, z in cuburi:
    for fatacub in fetecub:
        (x1, y1, z1), (x2, y2, z2), (x3, y3, z3), (x4, y4, z4) = sorted(fatacub)
        latura = (
        (x1 + x, y1 + y, z1 + z), (x2 + x, y2 + y, z2 + z), (x3 + x, y3 + y, z3 + z), (x4 + x, y4 + y, z4 + z))
        # print (latura)
        if latura in vulcan:
            dubluri.add(latura)

        vulcan.add(latura)

vulcan.difference_update(dubluri)
print('Rezultat partea 1 a ->', len(vulcan))

altecuburi = []

# generam cuburi care nu apartin inputului , maxim posibile

for x in range(minx, maxx + 1):
    for y in range(miny, maxy + 1):
        for z in range(minz, maxz + 1):
            if [x, y, z] in cuburi:
                None
            else:
                altecuburi.append([x, y, z])

print('Calculez , rabdare ,max 10 sec .....')
cuburinterior = []
for x, y, z in altecuburi:
    if not liber(x, y, z):
        cuburinterior.append([x, y, z])

print('terminat faza 1 , am gasit', len(cuburinterior), 'cuburi posibil interioare')

fetecomune = set()

mai = True

while mai:
    unu = len(cuburinterior)

    for x, y, z in cuburinterior:

        if veciniliberi(x, y, z):
            cuburinterior.remove([x, y, z])
    if unu == len(cuburinterior):
        mai = False

print('terminat faza 2 , am redus numarul de cuburi interioare la', len(cuburinterior))

for x, y, z in cuburinterior:
    for fatacub in fetecub:
        (x1, y1, z1), (x2, y2, z2), (x3, y3, z3), (x4, y4, z4) = sorted(fatacub)
        latura = (
        (x1 + x, y1 + y, z1 + z), (x2 + x, y2 + y, z2 + z), (x3 + x, y3 + y, z3 + z), (x4 + x, y4 + y, z4 + z))

        if latura in vulcan:
            fetecomune.add(latura)

print()
print('Rezultat partea 2 a ->', len(vulcan) - len(fetecomune))
