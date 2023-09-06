fr = open("zaznamy.txt", "r", encoding="utf-8")

#TODO 1. BOD
lines = len(fr.readlines())
print('Total Number of lines:', lines)

# TODO 2. BOD A 3. BOD
r = ''
list = []
list_res = []
with open('zaznamy.txt') as fp:
    for line in fp:
        x = line.split(' ')
        print(x[3])
        list.append(x[3])
    for i in list:
        x = i.replace(',','.')
        list_res.append(float(x))
    print(list_res)
    list_res.sort()
    print(list_res[-1])
    if list_res[-1] > 0:
        r = str(list_res[-1])
        r = '+' + str(list_res[-1])
    r = r.replace('.',',')
    print(r)

# TODO 4. BOD
with open('zaznamy.txt') as fp:
    for line in fp:
        x = line.split(' ')
        if r in x:
            print(x[0])

# TODO 5. BOD
calc = 0
count = 0
for i in list_res:
    calc += i
    count += 1
print(calc/count)






