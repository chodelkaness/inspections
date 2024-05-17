import unittest
from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_predict(self):
        response = self.app.post('/predict', json={
            'features': [750000, 3, 2, 250000, 375000, 1.5]
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('prediction', response.json)

    def test_find_similar_properties(self):
        response = self.app.post('/similar', json={
            'features': "1/1701 Centre Road, Oakleigh South $750000 3 2"
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('similar_properties', response.json)

if __name__ == "__main__":
    unittest.main()
