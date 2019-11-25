
def get_word():
    """gets the word from RandomWords module, creates word_dict and initial playfield_list with ----- """
    print("--- Plesae wait, while the computer selects the word ---")
    from random_word import RandomWords
    word = RandomWords().get_random_word().lower()
    if "-" in word:
        return get_word()
    else:
        word_dict = dict(enumerate(word))
        playfield_list = list(''.join(len(word)*"-"))
        return word, word_dict, playfield_list

def verify_playfield(word, playfield_list, wrong_letters):
    """Creates and prints playfield_str with remaining attempts, verifies, if the game continues"""
    playfield_str = ' '.join(playfield_list)

    if "-" in playfield_list:
        print(f"""Here is the playfield: {playfield_str}
    \nYou have {10-len(wrong_letters)} attempts left.""")
        play = True
        return play, playfield_str
    else:
        play = False
        print("*** The game is over. You won. ***")
        return play, False

def letter_input():
    """asks the letter from the player"""
    letter = input("Enter the letter you think the word may contain: ").lower()
    return letter

def letter_verification(letter, wrong_letters, right_letters):
    """verifies, if the letter input is letter"""
    if letter in wrong_letters or letter in right_letters:
        print(f"You have already tried '{letter}'. Please, try again.")
        letter = letter_input()
        letter = letter_verification(letter, wrong_letters, right_letters)
    elif not letter.isalpha():
        print("This is not a letter. Please, try again.")
        letter = letter_input()
        letter = letter_verification(letter, wrong_letters, right_letters)
    else:
        return letter


def letter_in_word(letter, word_dict, playfield_list, wrong_letters, right_letters):
    """Verifies, if the letter is in the word, adds it either to playfield_list or to wrong_letters"""
    letter_in_word = False
    for k, v in word_dict.items():
        if v == letter:
            right_letters.append(letter)
            letter_index = k
            playfield_list[letter_index] = letter            
            letter_in_word = True
    if letter_in_word:
        print(playfield_list)
        return playfield_list, wrong_letters, right_letters
    else:
        print(wrong_letters)        
        wrong_letters.append(letter)
        print(wrong_letters)     
        return playfield_list, wrong_letters, right_letters

def gibbet_build(wrong_letters):
    """Builds another piece of gibbet if wrong letter"""
    gibbet = {
        0 : """
            
            
            
            
            
            
        """, 
        1 : """
            
            
            
            
            
            
        ~~~~~~~""",
        2 : """
        +
        |
        |
        |
        |
        |
        ~~~~~~~""",
        3 : """
        +---.
        |
        |
        |
        |
        |
        ~~~~~~~""",
        4 : """
        +---.
        |   |
        |
        |
        |
        |
        ~~~~~~~""",
        5 : """
        +---.
        |   |
        |   O
        |
        |
        |
        ~~~~~~~""", 
        6 : """
        +---.
        |   |
        |   O
        |   |
        |
        |
        ~~~~~~~""",
        7 : """
        +---.
        |   |
        |   O
        | --|
        |
        |
        ~~~~~~~""", 
        8 : """
        +---.
        |   |
        |   O
        | --|--
        |
        |
        ~~~~~~~""", 
        9 : """
        +---.
        |   |
        |   O
        | --|--
        |  /
        |
        ~~~~~~~""", 
        10 : """
        +---.
        |   |
        |   O
        | --|--
        |  / \\
        |
        ~~~~~~~"""
        }
    
    
    print(gibbet[len(wrong_letters)])

def new_game():
    answer = input("Do you wish to play again? [ y / n ] ")
    answer.lower()
    if answer == "y":
        game()
    elif answer == "n":
        print("*** Thank you for the play. Goodbye. ***")


def game():
    wrong_letters = []
    right_letters = []
    word, word_dict, playfield_list = get_word()
    print("\nThe computer selected the word.", end=" ")
    play, playfield_str = verify_playfield(word, playfield_list, wrong_letters)
    print(playfield_str)
    while play:        
        letter = letter_input()
        letter = letter_verification(letter, wrong_letters, right_letters)
        playfield_list, wrong_letters, right_letters = letter_in_word(letter, word_dict, playfield_list, wrong_letters, right_letters)
 
        if len(wrong_letters) < 10:
            gibbet_build(wrong_letters)
            print(wrong_letters)
            if len(wrong_letters) > 0:
                print(f"Wrong letters, you already tried: {(' ,'.join(wrong_letters))}")
        else:
            print("*** The game is over. You lost. ***")
            break
        play, playfield_str = verify_playfield(word, playfield_list, wrong_letters)
    new_game()

game()