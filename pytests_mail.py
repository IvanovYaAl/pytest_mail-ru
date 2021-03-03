import pytest
import math

#parametrize tests
@pytest.mark.parametrize("num, output",[(1,17),(2,34),(3,51),(4,68)])
def test_multiplication_17(num, output):
   assert 17*num == output

@pytest.mark.parametrize("string, letters", [("pizza", 5), ("teacher", 7), ("RUSSIA", 6), ("cat", 3)])
def test_parametrize_words(string, letters):
    assert len(string) == letters

#str tests
def test_number_of_letters_eq_5():
    a = "pizza"
    assert len(a) == 5

def test_find_word_in_str():
    a = "So long story about The Dark Knight"
    assert a[8:13] == "story"

def test_get_letter_from_str():
    a = "I FOUND U"
    assert a[4] == "U"

#dict tests
def test_dict():
    dict = {"a": "pizza", "b": "rocks", "c": "Debra"}
    del dict["b"]
    assert len(dict) == 2

def test_find_word_dict():
    dict = {"qwerty": 1, "asdfgh": 2, "zxcvbn": 3}
    mypassword = "qwerty"
    assert mypassword in dict

def test_get_coupls_from_dict():
    dict1 = {a: a ** 2 for a in range(7)}
    dict2 = {3: 9, 4: 16}
    assert dict1[4] == dict2[4]

#negative tests
def test_er():
    try:
        num = -135
        assert math.log(num,[-4])
    except ValueError:
        pass

def test_er_str():
    try:
        let = "letters"
        ret = "letterss"
        assert let == ret
    except AssertionError:
        pass
