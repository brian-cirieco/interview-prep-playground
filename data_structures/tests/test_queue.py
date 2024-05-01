from unittest import TestCase
from data_structures.queue import Queue

class QueueTest(TestCase):

    def test_init(self):

        queue = Queue()

        self.assertIsNone(queue.head)
        self.assertIsNone(queue.tail)

    def test_push(self):

        queue = Queue()
        queue.push(1)

        self.assertIsNotNone(queue.head)
        self.assertIsNotNone(queue.tail)
        self.assertEqual(queue.head, queue.tail)

    def test_pop(self):

        test_val = 1

        queue = Queue()
        queue.push(test_val)

        self.assertEqual(queue.head.val, test_val)

        popped_val = queue.pop()

        self.assertEqual(test_val, popped_val)
        self.assertIsNone(queue.head)
        self.assertIsNone(queue.tail)

    def test_pop_when_empty(self):
        queue = Queue()
        
        result = queue.pop()

        self.assertIsNone(result)
