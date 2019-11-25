import Hangman
import pytest

def test_get_word():
    word, word_dict, playfield_list = Hangman.get_word()
    assert type(word) == str
    assert type(word_dict) == dict
    assert type(playfield_list) == list
    assert "-" not in word
    assert len(word) != 0 
    assert len(word) == len(word_dict)
    assert len(word) == len(playfield_list)

    word, word_dict, playfield_list = Hangman.get_word()
    return word_dict

def test_verify_playfield():
    play, playfield_str = Hangman.verify_playfield("word", ["-", "-", "-", "-"], [])
    assert playfield_str == "- - - -"
    assert play == True

    play, playfield_str = Hangman.verify_playfield("word", ["w", "o", "r", "d"], [])
    assert playfield_str == False
    assert play == False

def test_letter_verification():
    assert Hangman.letter_verification("a", [], []) == "a"

    with pytest.raises(OSError):
        Hangman.letter_verification("a", ["a"], [])

    with pytest.raises(AttributeError):
        Hangman.letter_verification(1, [], [])

def test_letter_in_word():
    word = "word"
    word_dict = dict(enumerate(word))
    playfield_list = list(''.join(len(word)*"-"))
    wrong_letters = []
    right_letters = []
    playfield_list, wrong_letters, right_letters = Hangman.letter_in_word("w", word_dict, playfield_list, wrong_letters, right_letters)
    assert playfield_list == ["w", "-", "-", "-"]
    assert wrong_letters == []
    assert right_letters == ["w"]

    playfield_list, wrong_letters, right_letters = Hangman.letter_in_word("q", word_dict, playfield_list, wrong_letters, right_letters)
    assert playfield_list == ["w", "-", "-", "-"]
    assert wrong_letters == ["q"]
    assert right_letters == ["w"]

def test_gibbet_build():
    assert Hangman.gibbet_build(["q", "e"]) == """
        +
        |
        |
        |
        |
        |
        ~~~~~~~"""

    