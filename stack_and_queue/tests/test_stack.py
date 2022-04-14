from stack_and_queue.stack import Stack, Node
import pytest


def test_instantiate_empty_stack():
    stack = Stack()
    actual = stack.top
    expected = None
    assert actual == expected

def test_push(stack):
  actual = stack.top.value
  expected = 2
  assert actual == expected

def test_pop(stack):
  actual = stack.pop()
  expected = 2
  assert actual == expected

def test_peek(stack):
  actual = stack.peek()
  expected = 2
  assert actual == expected

def test_is_empty():
  stack = Stack()
  actual = stack.is_empty()
  expected = True
  assert actual == expected

def test_pop_on_empty_stack():
    stack = Stack()
    actual = stack.pop()
    expected = "Stack is empty"
    assert actual == expected

def test_peek_on_empty_stack():
    stack = Stack()
    actual = stack.peek()
    expected = "Stack is empty"
    assert actual == expected

def test_pop_all_node(stack):
    stack.pop()
    stack.pop()
    stack.pop()
    actual = stack.is_empty()
    expected = True
    assert actual == expected

def test_peek_next_element(stack):
    stack.top = stack.top.next
    actual = stack.peek()
    expected = 3
    assert actual == expected
 
@pytest.fixture
def stack():
  stack = Stack()
  stack.push(5)
  stack.push(3)
  stack.push(2)
  return stack


#DONE# Can successfully push onto a stack
#DONE# Can successfully push multiple values onto a stack
#DONE# Can successfully pop off the stack
#DONE# Can successfully empty a stack after multiple pops
#DONE# Can successfully peek the next item on the stack
#DONE# Can successfully instantiate an empty stack
#DONE# Calling pop or peek on empty stack raises exception

  
  
  
