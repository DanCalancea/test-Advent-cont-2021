import sys, fileinput


class Robot():
    def __init__(self, ore, clay, obsidian):
        self.ore = ore
        self.clay = clay
        self.obsidian = obsidian


def initializare_blueprint(nr):

    global ore, clay, obsidian, geode, roboti, minerale

    ore = Robot(blueprint[nr][1], 0, 0)
    clay = Robot(blueprint[nr][2], 0, 0)
    obsidian = Robot(blueprint[nr][3], blueprint[nr][4], 0)
    geode = Robot(blueprint[nr][5], 0, blueprint[nr][6])
    roboti = ['ore', 'clay', 'obsidian', 'geode']
    minerale = ['ore', 'clay', 'obsidian', 'geode']
    for i in minerale:
        utilaje[i] = 0
        stocuri[i] = 0
    utilaje['ore'] = 1
    stocuri['ore'] = 1


def work(time, utilaj, stocur, posibilities):

    global geodemax, memo

    if time > TIME:
        return

    geodemax = max(geodemax, stocur['geode'] + utilaj['geode'])

    for j in roboti:
        stocur[j] += utilaj[j]

    for i in posibilities:
        utilajenew = utilaj.copy()
        stocurinew = stocur.copy()

        timenew = time

        if timenew + 1 > TIME: continue

        if i != 'nimic':
            utilajenew[i] += 1
            stocurinew['ore'] -= eval(i).ore
            stocurinew['clay'] -= eval(i).clay
            stocurinew['obsidian'] -= eval(i).obsidian

        unu = str(stocurinew['ore']) + '.' + str(stocurinew['clay']) + '.' + str(stocurinew['obsidian'])
        if unu in memo:
            posibilitiesnew = memo[unu]
        else:
            if stocurinew['ore'] <= 4:          # aici am limitat numarul de posibilitati pentru 'nimic'
                posibilitiesnew = ['nimic']     # viteza a crescut
            else:
                posibilitiesnew = []
            for i in roboti:
                if eval(i).ore <= stocurinew['ore'] and eval(i).clay <= stocurinew['clay'] and eval(i).obsidian <= \
                        stocurinew[
                            'obsidian']:
                    posibilitiesnew.append(i)
            if 'geode' in posibilitiesnew:
                posibilitiesnew = ['geode']
            else:
                if 'obsidian' in posibilitiesnew and stocurinew['clay'] > geode.clay and stocurinew['ore'] > geode.ore:
                    posibilitiesnew = ['obsidian']   # aici am introdus conditii noi deoarece gresea
            memo[unu] = posibilitiesnew              # la 1 blueprint din 30 !! ( la 24 in cazul meu )
                                                     # codul a devenit mai lent vizibil

        work(timenew + 1, utilajenew, stocurinew, posibilitiesnew)

    return


def sesiune(time, rang, operator, start):

    global TIME, memo, geodemax
    TIME = time
    total = start
    timpstart=2
    for i in range(rang):

        initializare_blueprint(i)
        geodemax = 0
        memo = dict()

        print('lucrez la blueprint', i + 1, end='')
        work(timpstart, utilaje, stocuri, ['nimic'])
        a = 1 if rang == 3 else blueprint[i][0]
        total = eval('total' + operator + 'geodemax*a')
        print(' -->', geodemax)

    print ()
    print('rezultat la partea ', start + 1, '-a', total)
    print()

# ------------------------------- input ----------------------------------------------

parsing = [' ore and ', 'Blueprint ', ':', ' Each ore robot costs ', ' Each clay robot costs ',
           ' Each obsidian robot costs ', ' Each geode robot costs ', ' ore.', ' clay.', ' obsidian.']

if len(sys.argv) > 1:
    fil = open(sys.argv[1])
else:
    fil = fileinput.input(files='intrari19a22.txt')

blueprint = []

for line in fil:
    line = line.strip()
    for i in parsing:
        line = line.replace(i, ',')

    line = line.replace(',,', ',')
    line = line[1:-1]
    blueprint.append([int(x) for x in line.split(',')])

# ------------------------------- input ----------------------------------------------
stocuri = dict()
utilaje = dict()

sesiune(24, len(blueprint), '+', 0)  # partea 1
sesiune(32, 3, '*', 1)  # partea 2
