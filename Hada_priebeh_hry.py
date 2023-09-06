fr = open("hada.txt", "r", encoding="utf-8")

# TODO 1. BOD
lines = len(fr.readlines())
print('Total Number of lines:', lines)

# TODO 2. BOD
max = 0
with open('hada.txt') as fp:
    for line in fp:
        if len(line) > max:
            max = len(line)
    print(max)  # The comma to suppress the extra new line char

# TODO 3. BOD
kopia_fr = open("hada_kopia.txt", "w", encoding="utf-8")

# TODO 4. BOD
spacer = 0
counter = ''
char = ''
with open('hada.txt') as fp:
    for line in fp:
        counter = ''
        char = ''
        if spacer > 0:
            kopia_fr.write('\n')
        else:
            spacer += 1
        for i in line:
            if i == char:
                counter += 1
            else:
                kopia_fr.write(char+str(counter))
                char = i
                counter = 1
