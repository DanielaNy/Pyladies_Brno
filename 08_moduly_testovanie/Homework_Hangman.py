import sys
from random_word import RandomWords

r = RandomWords()
word = r.get_random_word().lower()

word_list = list(word)
lines = len(word)*'-'
lines_list =list(lines)
word_dict = dict(enumerate(word))
counts = len(word)+5
counts_to_end = counts

print(f"I am thinking of a word. What word is it?: \n {lines}")

while counts_to_end > 0:
    if '-' in lines_list:   
        print(counts_to_end, " guesses available")
        letter = input("Guess a letter: ").lower()
        
        if not letter.isalpha() or len(letter) != 1:
            print("Your input is not correct. Try again.")
        else:
            counts_to_end = counts_to_end - 1
            letter = letter.lower()            
            x = 0
            for k, v in word_dict.items():
                if v == letter:
                    letter_index = k
                    lines_list[letter_index] = letter
                    x += 1
                    if x == 1:
                        print(f"Yes, the letter '{letter}' is in my word".format(letter))                    
            print("".join(lines_list))        
            if not x:
                print(f"No, the letter '{letter}' is not in my word".format(letter))   
    else:
        print("You won! :)")
        sys.exit()

print("You guessed for", counts," times already. You lost :( \nThe word was:", word)
     