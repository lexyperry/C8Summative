import unittest
from app import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_get_inventory(self):
        response = self.client.get('/inventory')
        self.assertEqual(response.status_code, 200)

    def test_create_item(self):
        response = self.client.post('/inventory', json={
            "name": "Test Product", "stock": 5, "price": 1.99
        })
        self.assertEqual(response.status_code, 201)

if __name__ == "__main__":
    unittest.main()
