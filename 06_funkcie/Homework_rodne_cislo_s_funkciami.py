answer = input("""Zadaj rodne cislo v tvare s lomitkom
(spravny format: 6 cislic, lomitko, 4 cislice)\n
Rodne cislo: """)

number = False
string_number = False
birth = False

def formatcheck(answer):
    """Function to check if the format is right. 
    6 numbers, /, 4 numbers"""
    if len(answer) == 11:
        if answer[6] == "/":
            try:
                global number
                number = int(answer[0:6] + answer[7:11])
                return True   
            except ValueError:
                return False
        else:
            return False   
    else:
        return False

def divisible_by_11(number):
    if number == False:
        return 'NA'
    elif number % 11 == 0:
        global string_number
        string_number = str(number)
        return True
    else:
        return False

def male_female(string_number):
    if string_number == False:
        return 'NA'
    elif string_number[2] == "5" or string_number[2] == "6":
        return 'zena'
    elif string_number[2] == "0" or  string_number[2] == "1":
        return 'muz'
    else:
        return 'NA'

def birth_date(string_number):
    if male_female(string_number) == 'zena':
        birth = string_number[4:6] + ". " + str(int(string_number[2:4])-50) + ". 19" + string_number[0:2]
        return birth
    elif male_female(string_number) == 'muz':
        birth = string_number[4:6] + ". " + string_number[2:4] + ". 19" + string_number[0:2]
        return birth
    else:
        return 'NA'

print(f'\na) Format cisla: {formatcheck(answer)}'.format(formatcheck(answer)))
print(f'b) Delitelne 11: {divisible_by_11(number)}'.format(divisible_by_11(number)))
print(f'c) Datum narodenia: {birth_date(string_number)}'.format(birth_date(string_number)))
print(f'd) Pohlavie: {male_female(string_number)}'.format(male_female(string_number)))
