import sys, fileinput


if len(sys.argv) > 1:
    fil = open(sys.argv[1])
else:
    fil = fileinput.input(files='intrari6p2.txt')  # 2192039569602, 3849876073

MARKER=14

for line in fil:

    line = line.replace('\n', '')
    for j in range(MARKER,len(line)):
        alfa={line[x] for x in range(j-MARKER,j)}
        if len(alfa)==MARKER:
            print (j)
            break