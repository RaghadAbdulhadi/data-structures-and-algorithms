import pytest
from hashtable.hashtable import Hashtable

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

def test_collisions(hashtable):
    pass






@pytest.fixture
def hashtable():
    t = Hashtable(size=20)
    t.set('march 6', 300)
    t.set('april 6', 300)
    t.set('march 6', 300)
    t.set('march 4', 600)
    t.set('march 5', 1000)
    return t