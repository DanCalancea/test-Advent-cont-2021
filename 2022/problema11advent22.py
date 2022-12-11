import sys, fileinput

if len(sys.argv) > 1:
    fil = open(sys.argv[1])
else:
    fil = fileinput.input(files='intrari11p22.txt')

parsing = ['Monkey ', 'Starting items: ', 'Operation: new = old ',
           'Test: divisible by ', 'If true: throw to monkey ', 'If false: throw to monkey ']

monkey = []
step = 0
for line in fil:
    line = line.strip()
    if len(line) == 0: continue
    line = line.replace(parsing[step], '')

    if step == 1: a1 = [int(x) for x in line.split(',')]
    if step == 2:
        unu, doi = line.split()
        if unu == '+': a2 = [True, False, False, int(doi)]
        if unu == '*':
            if doi == 'old':
                a2 = [False, False, True, 1]
            else:
                a2 = [False, True, False, int(doi)]
    if step == 3: a3 = int(line)
    if step == 4: a4 = int(line)
    if step == 5: a5 = int(line)

    step += 1
    if step == 6:
        step = 0
        monkey.append([0, a1, a2, a3, a4, a5])

multiplu = 1

for membru in monkey:
    multiplu *= membru[3]
print(multiplu)

print(monkey)
RUNDE = 10000  # de pus 20 pentru partea 1---------------------------------------------------------
for i in range(RUNDE):
    print(i, '/', RUNDE)
    for membru in monkey:
        for marfa in membru[1]:

            if membru[2][0]: worry = marfa + membru[2][3]
            if membru[2][1]: worry = marfa * membru[2][3]
            if membru[2][2]: worry = marfa * marfa
            if worry > multiplu:
                worry = multiplu + worry % multiplu
          # worry=worry//3 uncomment for partea 1----------------------------------------------------
            if worry % membru[3] == 0:
                monkey[membru[4]][1].append(worry)
            else:
                monkey[membru[5]][1].append(worry)
            membru[0] += 1
        membru[1] = []

scor = []
for membru in monkey:
    scor.append(membru[0])

print(sorted(scor)[-1] * sorted(scor)[-2])
