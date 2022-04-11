# Data Structure:
Is a way to deal with data (organize, merge, create, modify)

# Linked list
```python
{
    "head": {
        "value": 1,
        "next": {
            "value": 2,
            "next": {
                "value": 3
                "next": None
            }
        }
    }
}
```

# Stack
```python
{
    "top":{
        "value":3
        "next": {
            "value":2
            "next": {
                "value":1
                "next": None
            }
        }
    }
}
```

# Queue
```python
{
    "head": {
        "value": 1,
        "next": {
            "value": 2,
            "next": {
                "value": 3
                "next": None
            }
        }
    }
}
```

# Test Stack

```python
import EmptyStackException
def test_init_stack():
    stack = Stack()
    assert stack.top == None

def test_push_stack():
    stack = Stack()
    stack.push(5)
    assert stack.top == 5

def test_push__two_nodes(stack_with_two_nodes):
    assert stack_with_two_nodes.value == 7
    assert stack_with_two_nodes.value == 5

def test_stack_is_empty():
    with pytest.raises(EmptyStackException):
        stack = Stack()
        stack.pop()
@pytest.fixtures
def stack_with_two_nodes():
    stack = Stack()
    stack.push(5)
    stack.push(7)
    return stack

```

# Intialize Stack

```python
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    class Stack: 
        def __init__(self) -> None:
            self.top = None
        
        def push(self, value):
            if self.top == None:
                raise EmptyStackException("Popping from empty stack is not allowed")
            node = Node(value)
            self.next = self.top
            self.top = node

    class EmptyStackException(Exception):
        pass




```