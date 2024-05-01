from unittest import TestCase
from ..queue2 import Queue2

class TestQueue2(TestCase):

    def test_init(self):

        queue = Queue2()

        self.assertIs(len(queue.items), 0)

    def test_enqueue(self):

        queue = Queue2()

        queue.enqueue(1)

        self.assertIn(1, queue.items)

    def test_dequeue(self):

        queue = Queue2()

        queue.enqueue(1)
        self.assertIn(1, queue.items)
        self.assertIs(len(queue.items), 1)

        popped_item = queue.dequeue()
        self.assertNotIn(popped_item, queue.items)
        self.assertIs(len(queue.items), 0)

    def test_dequeue_with_multiple_values(self):

        queue = Queue2()

        first_item = 1
        second_item = 2

        queue.enqueue(first_item)
        queue.enqueue(second_item)
        self.assertListEqual([1, 2], queue.items)

        popped_item = queue.dequeue()

        self.assertEqual(first_item, popped_item)
        self.assertNotIn(first_item, queue.items)
        self.assertIn(second_item, queue.items)

    def test_front(self):

        queue = Queue2()
        queue.enqueue(1)

        self.assertIs(queue.items[0], queue.front())
    
    def test_rear(self):

        queue = Queue2()
        queue.enqueue(1)

        self.assertIs(queue.items[0], queue.rear())