

max = None
min = None
while True :
    sNum = input('Enter a number: ')
    if sNum == 'done':
        break
    try:
        iNum = int(sNum)
    except:
        print('Invalid input')
        continue
    if max is None :
        max = iNum
    if min is None :
        min = iNum
    elif iNum > max :
        max = iNum
    elif iNum < min :
        min = iNum


print('Maximum is',max)
print('Minimum is',min)
