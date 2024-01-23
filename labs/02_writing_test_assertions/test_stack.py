from unittest import TestCase
from stack import Stack

class TestStack(TestCase):
    """Test cases for Stack"""

    def setUp(self):
        """Setup before each test"""
        self.stack = Stack()

    def tearDown(self):
        """Tear down after each test"""
        self.stack = None

    def test_push(self):
        """Test pushing an item into the stack"""
        self.stack.push(10)
        self.assertEqual(self.stack.peek(), 10)
        self.stack.push(1)
        self.stack.push(-9)
        self.assertEqual(self.stack.peek(), -9)

    def test_pop(self):
        """Test popping an item of off the stack"""
        self.stack.push(10)
        self.stack.push(2)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.peek(), 10)
        self.assertEqual(self.stack.pop(), 10)
        self.assertTrue(self.stack.is_empty())

    def test_peek(self):
        """Test peeking at the top the stack"""
        self.stack.push(10)
        self.assertEqual(self.stack.peek(), 10)
        self.stack.push(4)
        self.stack.push(1)
        self.assertEqual(self.stack.peek(), 1)
        self.stack.pop()
        self.assertEqual(self.stack.peek(), 4)


    def test_is_empty(self):
        """Test if the stack is empty"""
        self.assertTrue(self.stack.is_empty())
        self.stack.push(5)
        self.assertFalse(self.stack.is_empty())
        self.stack.pop()
        self.assertTrue(self.stack.is_empty())
