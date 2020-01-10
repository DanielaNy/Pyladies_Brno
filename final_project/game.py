import sqlite3
import os
from random import choice

filename_txt = "user" + "_file.txt"
filename_db = "user" + "_file.db"

levels = [0, 1, 2, 0, 0, 1, 0, 0, 0, 1]
words = {levels[0] : {}, levels[1] : {}, levels[2] : {}}
chosen = None
chosen_list = []

connection = sqlite3.connect("./user/" + filename_db)
cursor = connection.cursor()
    

def close_connection():
    connection.commit()
    connection.close()

def create_table():
    """creates a table 'username' for the user if it was not yet created"""
    cursor.execute("""CREATE TABLE IF NOT EXISTS username(Unknown_Word TEXT, Known_Word TEXT, Level INTEGER)""")
    connection.commit()
    return cursor

def new_words_from_text_file():
    """appends new words from the text file to the database, if user_textfile.txt uploaded"""
    if os.path.exists('./user/user_file.txt'):
        with open("./user/"+filename_txt) as user_file:
            for line in user_file:     
                line = line.rstrip()
                uploaded_words = line.split("; ")       # list
                cursor.execute("""INSERT INTO username(Unknown_Word, Known_Word, Level) VALUES (?, ?, ?)""", 
                                                            (uploaded_words[0], uploaded_words[1], int(0)))
        connection.commit()
        #os.remove('./user/user_file.txt')
        print("New words added to the \'username\' table from .txt file:")
        print(uploaded_words)

    else:
        print("No new words were added to the \'username\' table.")
        pass
    return cursor

def print_all_words_from_database():
    print("\n-------------------------- all words in table below ------------------------------")
    all_words = connection.execute("SELECT Unknown_Word, Known_Word, Level FROM username")
    for word in all_words:
        print(str(word)+"all")
    print("-------------------------- all words in table above ------------------------------\n")

def words_to_dictionaries():
    """adds the words to dictionaries according to knowledge level --> words = dict"""
    for idx, words_idx in words.items():
        #print(str(idx))        
        words_idx = dict(connection.execute("SELECT Unknown_Word, Known_Word FROM username WHERE Level =?", str(idx)))
        words[idx] = words_idx
        # for k, v in words_idx.items():
        #     print(k, ": ", v)
    return words

def select_word_to_test():
    """slects random word from dict "word" according to algorithm"""    
    for lvl in levels:
        for k, v in words.items():
            if k == lvl:
                print("from level:", lvl)       # to check
                a = dict(list(words.values())[lvl])
                try:
                    chosen = choice(list(a.keys()))
                    print(chosen)       # this is to be shown on web site
                    chosen_list.append(chosen)                 
                except IndexError:
                    pass
    return chosen_list


def prepare_game():
    """starts the game - creates the connection to database, import words"""
    connection = sqlite3.connect("./user/" + filename_db)
    cursor = connection.cursor()
    

    cursor = create_table()
    print_all_words_from_database()             # to check
    cursor = new_words_from_text_file()
    words = words_to_dictionaries()
    print(words)                                # to check
    chosen_list = select_word_to_test()
    print(chosen_list)                          # to check
    return connection, cursor, words, chosen_list

def play_game():

    # END
    close_connection()


# MAIN LOGIC

# if __name__ == "__main__":
#     #cursor.execute("""DROP TABLE IF EXISTS username""")
#     create_table()
#     print_all_words_from_database()             # to check
#     new_words_from_text_file()
#     words_to_dictionaries()
#     print(words)                                # to check
#     select_word_to_test()
#     print(chosen)
#     # END
#     close_connection()


