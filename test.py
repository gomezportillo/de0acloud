import unittest
import server

class TestMyServer(unittest.TestCase):

    def test_first(self):
        response = server.hello()
        self.assertIn('Hello', response, "Hello was not found in response")

if __name__ == '__main__':
    unittest.main()
