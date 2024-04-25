from typing import Union, List

class Node:

    def __init__(self, value: int):
        self.val = value
        self.next = None

class Stack:

    def __init__(self, values: List[int] = None):
        self.head = None
        
        if not values or len(values) is 0:
            return
        
        for val in values:
            self.push(val)
    
    def push(self, value: int) -> None:
        node = Node(value)
        node.next = self.head
        self.head = node

    def pop(self) -> Union[int, None]:
        if not self.head:
            return None
        
        val = self.head.val
        self.head = self.head.next
        return val
    
    def print(self) -> None:
        current = self.head

        while current:
            print(current.val)
            current = current.next
        print('\n')

test_stack = Stack([1, 2, 3, 4, 5])

test_stack.print()
print(test_stack.pop())
test_stack.print()
print(test_stack.pop())
test_stack.print()
print(test_stack.pop())
test_stack.print()
print(test_stack.pop())
test_stack.print()
print(test_stack.pop())

test_stack.print()

test_stack.push(-1)
test_stack.print()
