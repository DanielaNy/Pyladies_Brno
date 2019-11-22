number = input('enter a number: ')

try:
    number = float(number)
    print('Number is float')
    print(type(number))
    if number > 0:
        print('Number is greater than 0.')
    elif number == 0:
        print('Number is 0.')
    else:
        print('Number is smaller than 0.')

except ValueError:    
    try:
        number = str(number)
        print('This is string, not a number')
    except ValueError:
        pass