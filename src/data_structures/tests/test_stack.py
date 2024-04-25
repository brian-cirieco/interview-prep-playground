import unittest

from stack import Stack

test_values = [1, 2, 3, 4, 5]

class StackTest(unittest.TestCase):

    def test_init_no_values(self):

        stack = Stack()

        self.assertIsNone(stack.head)

if __name__ == '__main__':
    unittest.main()