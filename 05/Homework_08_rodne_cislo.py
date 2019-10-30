answer = input("""Zadaj rodne cislo v tvare s lomitkom:
\n(spravny format: 6 cislic, lomitko, 4 cislice)\n""")

if len(answer) == 11:
    lengthcheck = True
    if answer[6] == "/":
        try:
            number = int(answer[0:6] + answer[7:11])
            print(number)
            if number % 11 == 0:
                numbercheck = True
                string_number = str(number)
                if string_number[2] == 5 or 6:
                    sex = 'zena'
                    birth = string_number[4:6] + ". " + str(int(string_number[2:4])-50) + ". 19" + string_number[0:2]
                elif string_number[2] == 0 or 1:
                    sex = 'muz'
                    birth = string_number[4:6] + ". " + string_number[2:4] + ". 19" + string_number[0:2]
                else:
                    numbercheck = False         
            else:
                numbercheck = False
        except ValueError:
            numbercheck = False
            lengthcheck = False        
    else:
        print('Zadany vstup nie je rodne cislo, neobsahuje spravny pocet znakov')        
else:
    lengthcheck = False

if lengthcheck and numbercheck and birth and sex:
    print(f"""
    \n a) Format cisla: {lengthcheck}
    \n b) Delitelne 11: {numbercheck}
    \n c) Datum narodenia: {birth}
    \n d) Pohlavie: {sex}""".format(lengthcheck, numbercheck, birth, sex)
    )
elif lengthcheck and numbercheck:
    print(f"""
    \n a) Format cisla: {lengthcheck}
    \n b) Delitelne 11: {numbercheck}
    \n c) Datum narodenia: NA
    \n d) Pohlavie: NA""".format(lengthcheck, numbercheck)
    )
else:
    print(f"""
    \n a) Format cisla: {lengthcheck}
    \n b) Delitelne 11: NA
    \n c) Datum narodenia: NA
    \n d) Pohlavie: NA""".format(lengthcheck)
    )
