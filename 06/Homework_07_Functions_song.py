song = """
    I am a passenger
    And I ride and I ride
    I ride through the city's backside
    I see the stars come out of the sky
    Yeah, they're bright in a hollow sky
    You know it looks so good tonight
    I am the passenger
    I stay under glass
    I look through my window so bright
    I see the stars come out tonight
    I see the bright and hollow sky
    Over the city's ripped-back sky
    And everything looks good tonight
    Singin' la-la-la-la-la-la-la-la
    La-la-la-la-la-la-la-la
    La-la-la-la-la-la-la-la, la-la
    Get into the car
    We'll be the passenger
    We'll ride through the city tonight
    See the city's ripped backsides
    We'll see the bright and hollow sky
    We'll see the stars that shine so bright
    The sky was made for us tonight
    Oh, the passenger
    How, how he rides
    Oh, the passenger
    He rides and he rides
    He looks… 
    """

number_of_k = 0

for letter in song:
    if letter == 'k':
        number_of_k +=1
print(song)
print(f"Number of \'k\'-s in the song \'The Passenger\' by Iggy Popp is: {number_of_k}.".format(number_of_k))
