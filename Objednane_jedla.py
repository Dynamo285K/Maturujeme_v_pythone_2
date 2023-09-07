fr = open("objednane_jedla.txt", "r", encoding="utf-8")

# TODO 1. BOD
lines = len(fr.readlines())
print('Total Number of lines:', lines)

# TODO 2. BOD
z = 0
c = 0
m = 0
o = 0
with open('objednane_jedla.txt') as fp:
    for line in fp:
        x = line.split(' ')
        for i in x:
            for r in i:
                if r == 'z':
                    z += 1
                elif r == 'c':
                    c += 1
                elif r == 'm':
                    m += 1
                elif r == 'o':
                    o += 1
    print(z,c,m,o)

# TODO 3. BOD
if z < 20:
    print('z')
else:
    print('dostatok stravnikov pre jedlo z')
if c < 20:
    print('c')
else:
    print('dostatok stravnikov pre jedlo c')
if m < 20:
    print('m')
else:
    print('dostatok stravnikov pre jedlo m')
if o < 20:
    print('o')
else:
    print('dostatok stravnikov pre jedlo o')

# TODO 4. BOD
