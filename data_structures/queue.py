from typing import List
from .node import Node

class Queue:
    """Queue data structure of variable size."""

    def __init__(self, values: List[int] = None):

        self.head: Node = None
        self.tail: Node = None

        if values is None or len(values) == 0:
            return
        
        for val in values:
            self.push(val)

    def push(self, val):

        node = Node(val)

        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = Node(val)

    def pop(self):
        if self.head is None:
            return
        val = self.head.val
        self.head = self.head.next
        return val
    
    def print(self):
        current = self.head
        while current:
            print(current.val)
            current = current.next