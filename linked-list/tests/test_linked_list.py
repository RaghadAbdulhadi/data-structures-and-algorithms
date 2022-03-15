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

def test_insert_at_beg_to_existing_linked_list(ll):
    ll.insert_at_beginning("Raghad")
    actual = ll.to_string()
    expected = "{ Raghad } -> { Gheed } -> None"
    assert actual == expected

def test_value_exists_in_linked_list(ll):
    actual = ll.includes("Rund")
    expected = False
    assert actual == expected

def test_insert_after_last_node(ll):
    ll.insert_at_beginning("Omar")
    ll.insert_at_beginning("Raghad")
    ll.insert_after("Gheed", "Jood")
    actual = ll.to_string()
    expected = "{ Raghad } -> { Omar } -> { Gheed } -> { Jood } -> None"
    assert actual == expected

def test_insert_after_any_node(ll):
    ll.insert_at_beginning("Omar")
    ll.insert_at_beginning("Raghad")
    ll.insert_after("Omar", "Jood")
    actual = ll.to_string()
    expected = "{ Raghad } -> { Omar } -> { Jood } -> { Gheed } -> None"
    assert actual == expected

def test_insert_before_last_node(ll):
    ll.insert_at_beginning("Omar")
    ll.insert_at_beginning("Raghad")
    ll.insert_before("Gheed", "Jood")
    actual = ll.to_string()
    expected = "{ Raghad } -> { Omar } -> { Jood } -> { Gheed } -> None"
    assert actual == expected

def test_insert_before_any_node(ll):
    ll.insert_at_beginning("Omar")
    ll.insert_at_beginning("Raghad")
    ll.insert_before("Omar", "Jood")
    actual = ll.to_string()
    expected = "{ Raghad } -> { Jood } -> { Omar } -> { Gheed } -> None"
    assert actual == expected

def test_insert_node_to_end_linked_list(ll):
    ll.append("Jood")
    actual = ll.to_string()
    expected = "{ Gheed } -> { Jood } -> None"
    assert actual == expected

def test_insert_nodes_to_end_linked_list(ll):
    ll.append("Jood")
    ll.append("Raghad")
    ll.append("Omar")
    actual = ll.to_string()
    expected = "{ Gheed } -> { Jood } -> { Raghad } -> { Omar } -> None"
    assert actual == expected

def test_remove_node(ll):
    ll.append("Jood")
    ll.append("Raghad")
    ll.remove_at(0)
    ll.append("Omar")
    actual = ll.to_string()
    expected = "{ Jood } -> { Raghad } -> { Omar } -> None"
    assert actual == expected





@pytest.fixture
def ll():
    ll = linked_list()

    ll.insert_at_beginning("Gheed")

    return ll




