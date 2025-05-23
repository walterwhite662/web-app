import unittest
from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        # Set up a test client for the Flask application
        self.client = app.test_client()

    def test_home(self):
        # Send a GET request to the root URL
        response = self.client.get("/")
        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Assert that the response data matches the expected output
        self.assertEqual(response.data.decode(), "Hello, World!")

if __name__ == "__main__":
    unittest.main()
