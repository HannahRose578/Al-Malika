import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_get_books(self):
        response = self.app.get('/books')
        self.assertEqual(response.status_code, 200)

    def test_get_books_by_genre(self):
        response = self.app.get('/books/genre/Science Fiction')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()