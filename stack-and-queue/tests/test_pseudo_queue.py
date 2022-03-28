from stack_and_queue.pseudo_queue import PseudoQueue
from stack_and_queue.stack import Stack
import pytest

def test_enqueue(pseudo):
    actual = pseudo.to_string()
    expected = "{ Gheed } -> { Raghad } -> { Jood } -> { Omar } -> None"
    assert actual == expected

# def test_dequeue():
#     pass

# def test_empty_pseudo_queue():
#     pass


@pytest.fixture
def pseudo():
    pseudo = PseudoQueue()
    pseudo.enqueue("Gheed")
    pseudo.enqueue("Raghad")
    pseudo.enqueue("Jood")
    pseudo.enqueue("Omar")
    return pseudo