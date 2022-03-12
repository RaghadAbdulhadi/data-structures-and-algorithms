import pytest
from linked_list.linked_list import linked_list, Node


def test_head_value_in_empty_linked_list():
    ll = linked_list()
    expected = None
    actual = ll.head
    assert actual == expected

def test_empty_linked_list():
    ll = linked_list()
    actual = ll.to_string()
    expected = "Linked list is empty"
    assert actual == expected

def test_insert_to_empty_linked_list(ll):
    actual = ll.to_string()
    expected = "{ Gheed } -> None"
    assert actual == expected

def test_insert_to_existing_linked_list(ll):
    ll.insert("Raghad")
    actual = ll.to_string()
    expected = "{ Raghad } -> { Gheed } -> None"
    assert actual == expected

def test_value_exists_in_linked_list(ll):
    actual = ll.includes("Rund")
    expected = False
    assert actual == expected

def test_insert_to_end_linked_list(ll):
    ll.insert_at_end("Jood")
    actual = ll.to_string()
    expected = "{ Gheed } -> { Jood } -> None"
    assert actual == expected


@pytest.fixture
def ll():
    ll = linked_list()
    ll.insert("Gheed")
    return ll




