try:
    sleeping_hours = float(input('How many hours do you sleep per day in average? '))
    if sleeping_hours > 24:
        print('Hello from Earth!')
    elif sleeping_hours > 23:
        print('What can you do in less than 1 hour?!')
    elif sleeping_hours > 9:
        print('I suppose you are seriously ill. You should see a medical doctor.')
    elif sleeping_hours >= 7:
        print('You seem in a right sleeping condition.')
    elif sleeping_hours > 4:
        print('You should spend less money on coffee/energy drinks and get some sleep for free!.')
    else:
        print('What are you on?')
except ValueError:
    print('That is not a number')