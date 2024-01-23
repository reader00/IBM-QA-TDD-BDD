from unittest import TestCase
from stack import Stack


class StackTestCase(TestCase):
    def setUp(self):
        self.stack = Stack()

    def tearDown(self):
        self.stack = None

    def test_push(self):
        self.stack.push(9)
        self.assertEqual(self.stack.peek(), 9)

    def test_pop(self):
        self.stack.push(9)
        self.assertEqual(self.stack.pop(), 9)
        self.assertTrue(self.stack.isEmpty())
