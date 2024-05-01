from typing import List
from .node import Node

class Queue:
    """Queue data structure of variable size."""

    def __init__(self):

        self.head: Node = None
        self.tail: Node = None

    def push(self, val):

        node = Node(val)

        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = Node(val)

    def pop(self):
        if self.head is None:
            print("Queue is empty")
            return None
        
        val = self.head.val
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return val
    
    def print(self):
        current = self.head
        while current:
            print(current.val)
            current = current.next