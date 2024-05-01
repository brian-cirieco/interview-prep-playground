import unittest
from typing import List
from data_structures.stack import Stack

test_values = [1, 2, 3, 4, 5]

def createStackWithValues():
    stack = Stack()
    for value in test_values:
        stack.push(value)
    
    return stack

class StackTest(unittest.TestCase):

    def test_init_no_values(self):

        stack = Stack()

        self.assertIsNone(stack.head)

    def test_as_list(self):

        stack = createStackWithValues()

        self.assertListEqual(stack.as_list(), test_values)

    def test_push(self):

        stack = Stack()

        stack.push(test_values[0])

        self.assertEqual(stack.head.val, test_values[0])

    def test_pop(self):

        stack = createStackWithValues()

        removed_val = stack.pop()

        self.assertNotIn(removed_val, stack.as_list())
