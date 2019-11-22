a = input("Enter the cube\'s side value in cm:")
if type(a) == int:
    b = True
else:
    b = False
#print(type(a))
surface = 6*a**2
volume = a**3


if a <= 0:
    print('The value you entered is wrong.')
elif b == False:
    print('This is not a value.')
else:
    print('The value you entered is ok.')
    print('The surface area of the cube with the side of', a, 'cm is', surface, 'cm2.')
    print('The volume of the cube with the side of', a, 'cm is', volume, 'cm3.')
#     print("The surface area of the cube with the side of {a} cm is {surface}.".format(a, surface))
#     print("The volume of the cube with the side of {a} cm is {volume}.".format(a, volume))
