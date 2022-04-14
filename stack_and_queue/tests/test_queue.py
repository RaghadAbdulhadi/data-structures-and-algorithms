from stack_and_queue.queue import Queue,Node
import pytest

def test_enqueue(queue):
  actual = queue.rear.value 
  expected = "Raghad"
  # actual = queue.front.value 
  # expected = "Jood"
  assert actual == expected

def test_is_empty():
    queue = Queue()
    actual = queue.is_empty()
    expected = True
    assert actual == expected
  
def test_peek(queue):
    actual = queue.peek()
    expected = "Jood"
    assert actual == expected

def test_instantiate_empty_queue():
    queue = Queue()
    actual = queue.front
    expected = None
    assert actual == expected

def test_peek_on_empty_queue():
    queue = Queue()
    actual = queue.peek()
    expected = "Queue is empty"
    assert actual == expected

def test_dequeue(queue):
    actual = queue.dequeue()
    expected = "Jood"
    assert actual == expected

def test_dequeue_all_nodes(queue):
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    actual = queue.is_empty()
    expected = True
    assert actual == expected

def test_dequeue_on_empty_queue():
    queue = Queue()
    actual = queue.dequeue()
    expected = "Queue is empty"
    assert actual == expected


@pytest.fixture
def queue():
    queue = Queue()
    queue.enqueue("Jood")
    queue.enqueue("Gheed")
    queue.enqueue("Raghad")
    return queue


#DONE# Can successfully enqueue into a queue
#DONE# Can successfully enqueue multiple values into a queue
#DONE# Can successfully dequeue out of a queue the expected value
#DONE# Can successfully peek into a queue, seeing the expected value
#DONE# Can successfully empty a queue after multiple dequeues
#DONE# Can successfully instantiate an empty queue
#DONE# Calling dequeue or peek on empty queue raises exception