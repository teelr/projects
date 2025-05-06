import unittest
from src.main import greet

class TestMain(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("AI World"), "Hello, AI World!")

if __name__ == "__main__":
    unittest.main()