import piskvorky, ai, util
from random import randint

# tests for tah function:

def test_tah_str_pole():
    pole = util.tah(0, "X", "--------------------")
    assert type(pole) == str

def test_tah_len_pole():
    pole = util.tah(0, "X", "--------------------")
    assert len(pole) == 20

def test_tah_right_symbol_placement():
    pole = util.tah(0, "X", "--------------------")
    assert pole[0] == "X"
    pole = util.tah(2, "s", pole)
    assert pole[0] == "X"
    assert pole[2] == "s"


# tests for tah_pocitaca function:

def test_tah_pocitaca_choose_place():
    pole = ai.tah_pocitaca("--------------------", False)
    assert pole.count("O") == 1
    assert pole.count("-") == 19


# tests for tah_hraca function - neda sa testovat, 
# len ak zakomentujem input v tah_hraca

# def test_tah_hraca_place_symbol():
#     pole = piskvorky.tah_hraca("--------------------", 2)
#     assert pole[2] == "X"
#     assert pole[0] == "-"

# def test_tah_hraca_assign_place():
#     pole = piskvorky.tah_hraca("--------------------", 8)
#     assert pole.count("X") == 1
#     assert pole.count("-") == 19


# tests for vyhodnot function

def test_vyhodnot_OOO():
    assert piskvorky.vyhodnot("-OOO----------------") == False

def test_vyhodnot_OOO():
    assert piskvorky.vyhodnot("XOOO---X------------") == False

def test_vyhodnot_XXX():
    assert piskvorky.vyhodnot("-------------XXX----") == False

def test_vyhodnot_other():
    assert piskvorky.vyhodnot("-OO-----------------") == None

def test_vyhodnot_other():
    assert piskvorky.vyhodnot("----X---------------") == None

def test_vyhodnot_other():
    assert piskvorky.vyhodnot("-O-----------------X") == None

def test_vyhodnot_other():
    assert piskvorky.vyhodnot("--------------------") == None


# tests for piskvorky function

def test_piskvorky():
    assert piskvorky.piskvorky("XOXOXO") == print("Dakujem za hru.") # no tak toto je daka podivnost, nechapem, ze to takto preslo :D
    assert piskvorky.piskvorky("XXX---") == print("Dakujem za hru.")
