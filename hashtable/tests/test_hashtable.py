import unittest
import pytest
from hashtable.hashtable import Hashtable, repeated_word, MyException

def test_hash():
    t = Hashtable()
    actual = t.hash("march 6")
    expected = 9
    assert actual == expected

def test_set_item(hashtable):
    actual = hashtable.table
    expected = [None, None, [['april 6', 300]], None, None, None, None, [['march 4', 600]], [['march 5', 1000]], [['march 6', 300], ['march 6', 300]], None, None, None, None, None, None, None, None, None, None]
    assert actual == expected

def test_get_item(hashtable):
    actual = hashtable.get('march 4')
    expected = 600
    assert actual == expected

def test_doesnt_contain_key(hashtable):
    actual = hashtable.contains('march 4')
    expected = True
    assert actual == expected

def test__contain_key(hashtable):
    actual = hashtable.contains('march 10')
    expected = False
    assert actual == expected

def test_keys_collection(hashtable):
    actual = hashtable.keys()
    expected = ['april 6', 'march 4', 'march 5', 'march 6', 'march 6']
    assert actual == expected

# Repeated words tests
def test_repeated_words_paragraph():
    string = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    actual = repeated_word(string)
    expected = "it"
    assert actual == expected

def test_repeated_words_phrase():
    string = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    actual = repeated_word(string)
    expected = "summer"
    assert actual == expected

def test_repeated_words_lower_upper_case():
    string = "Jordan, jordan"
    actual = repeated_word(string)
    expected = "jordan"
    assert actual == expected

def test_repeated_words_no_repeated_words():
    string = "Jordan"
    actual = repeated_word(string)
    expected = "No repeated words detected"
    assert actual == expected

class EmptyTree(unittest.TestCase):

    def test_empty_string(self):
        string = ""
        self.assertRaises(MyException, repeated_word, string)
    def test_empty_not_string(self):
        string = 0
        self.assertRaises(MyException, repeated_word, string)

@pytest.fixture
def hashtable():
    t = Hashtable(size=20)
    t.set('march 6', 300)
    t.set('april 6', 300)
    t.set('march 6', 300)
    t.set('march 4', 600)
    t.set('march 5', 1000)
    return t