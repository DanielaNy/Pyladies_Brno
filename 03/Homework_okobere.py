from random import randint

points = 0
name = input('Hello, what is your name? ')

choice = "y"

while choice == "y":
    print(f'You have currently {points} points. Do you wish to take another card? [y/n]'.format(name,points))
    choice = input()
    if choice == "y":
        x = randint(2, 10)
        print(f'Your next card is: {x}'.format(x))
        points = points+x          
        continue
    elif choice == "n":
        if points < 21:
            z = "less than"
            print(f'{name}, you gained {points} points, which is {z} 21. Congratulations!'.format(name, points, z))
            break
        elif points == 21:
            z = "equal to"
            print(f'{name}, you gained {points} points, which is {z} 21. Congratulations! You did your best.'.format(name, points, z))
            break
        else:
            z = "more than"
            print(f'{name}, you gained {points} points, which is {z} 21. You failed!'.format(name, points, z))
            break
    else:
        print('You need to enter "y" or "n"]')
        choice = 'y'
        continue

print('Goodbye :) ')


