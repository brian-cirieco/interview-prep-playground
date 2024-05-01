from typing import Union, List
from .node import Node

class Stack:

    def __init__(self):
        self.head = None
    
    def push(self, value: int) -> None:
        """appends value at tail of stack"""
        node = Node(value)
        node.next = self.head
        self.head = node
    
    def pop(self) -> Union[int, None]:
        """removes and returns last element of stack"""

        if not self.head:
            return None
        
        val = self.head.val
        self.head = self.head.next
        return val
    
    def as_list(self) -> List[int]:
        """copies values of stack and returns list"""

        current = self.head
        values = []

        while current:
            values.append(current.val)
            current = current.next

        values.reverse()
        return values

    def print(self) -> None:
        """prints values"""
        print(self.as_list())
