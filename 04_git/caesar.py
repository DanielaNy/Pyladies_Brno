input_key = input('What is your desired Caesar key? ')
while type(input_key) == str:
    try:
        k = int(input_key)
        if k <=0:
            print('You need to enter a positive integer nubmer.')
            input_key = input('What is your desired Caesar key? ')
            continue
        break
    except ValueError:
        print('You need to enter an integer nubmer.')
        input_key = input('What is your desired Caesar key? ')
        continue

print(f'Your Caesar key is {k}.'.format(k))

input_plaintext = input('Enter the text, you wish to encrypt with your Caesar key:\n')
ciphertext = ("")
for pi_character in input_plaintext:
    pi_ascii = ord(pi_character)
    if pi_ascii == 32:
        ci_ascii = pi_ascii
    else:
        ci_ascii = (pi_ascii + k%26) 
    ci_character = chr(ci_ascii)
    ciphertext = ciphertext + ci_character
print(f'Your encrypted text is:\n{ciphertext}'.format(ciphertext))
