import sys, fileinput


def verific(cimp, valoare):
    if cimp == 'ecl':
        if valoare in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):

            return True
        else:
            return False
    elif cimp == 'pid':
        if len(valoare) == 9 and valoare.isnumeric():
            return True
        else:
            return False
    elif cimp == 'hcl':
        if len(valoare) != 7 or valoare[0] != '#':
            return False
        if valoare[1:].isnumeric(): return True
        for x in valoare[1:]:
            if ord(x) < 97 or ord(x) > 102:
                if ord(x) < 48 or ord(x) > 57:
                    return False
        return True

    elif cimp == 'hgt':
        if not valoare[:-2].isnumeric(): return False
        if valoare[-2:] == 'cm':
            if 150 <= int(valoare[:-2]) <= 193:
                return True
            else:
                return False
        if valoare[-2:] == 'in':
            if 59 <= int(valoare[:-2]) <= 76:
                return True
            else:
                return False
        return False
    if len(valoare) != 4 or not valoare.isnumeric(): return False
    unu = int(valoare)
    if cimp == 'byr' and unu <= 2002 and unu >= 1920: return True
    if cimp == 'iyr' and unu <= 2020 and unu >= 2010: return True
    if cimp == 'eyr' and unu <= 2030 and unu >= 2020: return True
    return False


if len(sys.argv) > 1:
    fil = open(sys.argv[1])
else:
    fil = fileinput.input(files='intrari4.txt')

idcard = []
idcardinitial = ''

cardcapm = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')

for line in fil:  # citim

    line = line.replace('\n', '')
    if len(line) > 1:
        idcardinitial += ' ' + line
    else:
        idcard.append(idcardinitial)
        idcardinitial = ''

nr = 0

for card in idcard:
    cardi = card.split()
    este = True
    for camp in cardcapm:
        if not (camp + ':') in card:
            este = False
        else:
            for a in cardi:
                if a[0:3] == camp:
                    intrare = a[4:]
                    print(camp, intrare)
            print(verific(camp, intrare))
            if not verific(camp, intrare): este = False

    if este: nr += 1

print(nr)
