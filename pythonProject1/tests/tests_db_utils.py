import unittest
from db_utils import connect_to_db, execute_query, close_connection

class TestDBUtils(unittest.TestCase):

    def test_connection(self):
        connection = connect_to_db()
        self.assertIsNotNone(connection)

    def test_execute_query(self):
        connection = connect_to_db()
        query = "SELECT * FROM Books"
        result = execute_query(connection, query)
        self.assertIsNotNone(result)

    def test_close_connection(self):
        connection = connect_to_db()
        close_connection(connection)
        self.assertTrue(connection.is_closed)

if __name__ == '__main__':
    unittest.main()