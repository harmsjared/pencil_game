import random

names = ['John', 'Jack']
print('How many pencils would you like to use:')

while True:
    try:
        pencils = int(input())
        if pencils > 0:
            break
        else:
            print('The number of pencils should be positive')
    except ValueError:
        print('The number of pencils should be numeric')

print('Who will be the first (John, Jack):')
while True:
    turn = input()
    if turn not in names:
        print("Choose between 'John' and 'Jack'")
    else:
        break

while pencils > 0:
    print('|' * pencils)
    print(f"{turn}'s turn:")
    if turn == 'Jack':
        if pencils % 4 == 0:
            decrement = 3
        elif pencils % 4 == 3:
            decrement = 2
        elif pencils % 4 == 2:
            decrement = 1
        else:
            decrement = random.randint(1, min(3, pencils))
        print(decrement)
    else:
        while True:
            try:
                decrement = int(input())
                if 3 >= decrement > 0:
                    break
                else:
                    print("Possible values: '1', '2' or '3'")
            except ValueError:
                print("Possible values: '1', '2' or '3'")
    pencils -= decrement

    if pencils < 0:
        print('Too many pencils were taken')
        decrement = int(input())

        break

    if pencils == 0:
        break

    if turn == 'John':
        turn = 'Jack'
    else:
        turn = 'John'

if turn == 'John':
    turn = 'Jack'
else:
    turn = 'John'

print(f'{turn} won!')
