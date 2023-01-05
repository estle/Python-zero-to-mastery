money = 0
while 1:
    trans = input().split(' ')
    if trans[0] == 'D':
        money = money + int(trans[1])
    elif trans[0] == 'W':
        money = money - int(trans[1])
    elif input() == '':
        break
    print(f'Your current balance is: {money}')