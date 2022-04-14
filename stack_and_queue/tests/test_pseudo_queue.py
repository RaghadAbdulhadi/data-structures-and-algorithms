from stack_and_queue.pseudo_queue import PseudoQueue
from stack_and_queue.stack import Stack

def test_dequeue():
    pseudo = PseudoQueue()
    pseudo.enqueue("Omar")
    pseudo.enqueue("Jood")
    pseudo.enqueue("Raghad")
    pseudo.enqueue("Gheed")
    
    actual = pseudo.dequeue()
    expected = "Omar"
    assert actual == expected

def test_enqueue():
    pseudo = PseudoQueue()
    pseudo.enqueue("Omar")
    pseudo.enqueue("Jood")
    pseudo.enqueue("Raghad")
    pseudo.enqueue("Gheed")
    actual =pseudo.stack_one.top.value
    expected = "Gheed"
    assert actual == expected

def test_empty_pseudo_queue():
    pseudo = PseudoQueue()
    actual = pseudo.dequeue()
    expected = "Pseudo Queue is empty"
    assert actual == expected