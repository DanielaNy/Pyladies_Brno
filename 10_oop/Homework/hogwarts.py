import random

class Student():            # Jedna rodičovská třída, kde bude alespoň jeden atribut a jedna metoda
    def __init__(self, name):
        self.name = name

    def friends(self):
        friends = [None]
        print(f"{self.name}'s friends are: {friends}")

    def uniform(self):
        print(f"""Uniform: A black robe and a black pointed hat.""", end='')

class Gryffindor(Student):  # Dvě (nebo více) odvozených tříd
    house = "Gryffindor"
    def __init__(self, name):
        self.name = name

    def character(self):    # Obě odvozené třídy budou mít stejnou metodu, která bude dělat stejnou věc jiným způsobem (koťátko mňouká, štěňátko štěká)
        character_list = ["courage", "bravery", "nerve", "chivalry"]
        print("Valuable characters: ", character_list)

    def uniform(self):      # Druhá odvozená třída bude rozšiřovat metodu nadřazené třídy pomocí super()
        color =  'scarlet', 'gold'
        super().uniform()
        print(f"The uniform contains a crest in {color[0]} and {color[1]} colours of the {self.house}'s house.")

    def friends(self):      # Jedna odvozená třída bude kompletně přepisovat metodu nadřazené třídy
        friends = (self.house)+"'s students"
        print(f"{self.name}'s friends are: {friends}")
    
class Hufflepuff(Student): 
    house = "Hufflepuff"
    def __init__(self, name):
        self.name = name

    def character(self):   
        character_list = ["hard work", "patience", "justice", "loyalty"]
        print("Valuable characters: ", character_list)

    def uniform(self):      
        color =  'yellow', 'black'
        super().uniform()
        print(f"The uniform contains a crest in {color[0]} and {color[1]} colours of the {self.house}'s house.")

    def friends(self):      
        friends = (self.house)+"'s students"
        print(f"{self.name}'s friends are: {friends}")

class Ravenclaw(Student):
    house = "Ravenclaw"
    def __init__(self, name):
        self.name = name

    def character(self):   
        character_list = ["intelligence", "creativity", "learning", "wit"]
        print("Valuable characters: ", character_list)

    def uniform(self):      
        color =  'blue', 'bronze'
        super().uniform()
        print(f"The uniform contains a crest in {color[0]} and {color[1]} colours of the {self.house}'s house.")

    def friends(self):      
        friends = (self.house)+"'s students"
        print(f"{self.name}'s friends are: {friends}")

class Slytherin(Student):
    house = "Slytherin"
    def __init__(self, name):
        self.name = name

    def character(self):   
        character_list = ["ambition", "cunning", "leadership", "resourcefulness"]
        print("Valuable characters: ", character_list)

    def uniform(self):      
        color =  'green', 'silver'
        super().uniform()
        print(f"The uniform contains a crest in {color[0]} and {color[1]} colours of the {self.house}'s house.")

    def friends(self):      
        friends = (self.house)+"'s students"
        print(f"{self.name}'s friends are: {friends}")


def print_all_students(students):
    """creates and prints all students' info"""
    print(f"Number of students in Hogwarts: {len(students)}")
    print(f"Below, you can find a complete list of Hogwarts' students:")
    for student in students:
        print(f"\n {student.name}, from {student.house}")
        student.character()
        student.uniform()

def create_student(students):
    """creates a student according to input name, assigns house and appends to students' list"""
    answer = input("Do you wish a student to join Hogwarts? [y/n] ").lower()
    if answer == "y":
        name = input("Enter the student's name: ")
        name = name[0].upper()+name[1:].lower()
        house_choice = random.choice([Gryffindor, Hufflepuff, Ravenclaw, Slytherin])
        students.append(house_choice(name))
        again = True
        return students, again
    
    elif answer == "n":  
        again = False      
        return students, again
    else:
        print("I do not understand. Try again.")
        again = True
        return students, again

students = [Gryffindor("Harry"), Hufflepuff("Cedric"), Ravenclaw("Luna"), Slytherin("Draco")]
again = True
print(" *** WELCOME TO HOGWARTS, Hogwarts School of Witchcraft and Wizardry *** ")

while again:
    students, again = create_student(students)
print_all_students(students)
print("\nThank you for a visit. Goodbye.")
