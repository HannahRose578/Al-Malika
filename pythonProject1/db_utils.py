import pymysql
from pymysql.cursors import DictCursor
from config import DATABASE_CONFIG


def connect_to_db():
    try:
        connection = pymysql.connect(**DATABASE_CONFIG)
        return connection
    except pymysql.MySQLError as e:
        print(f"Error while connecting to MySQL: {e}")
        return None


def execute_query(connection, query, params=None):
    if connection is None:
        print("Connection is not established.")
        return None

    try:
        with connection.cursor(DictCursor) as cursor:
            cursor.execute(query, params)
            result = cursor.fetchall()
        return result
    except pymysql.MySQLError as e:
        print(f"Error while executing query: {e}")
        return None


def close_connection(connection):
    if connection:
        connection.close() 


# Example usage
# conn = connect_to_db()
# if conn:
#     result = execute_query(conn, "SELECT * FROM some_table")
#     print(result)
#     close_connection(conn)
