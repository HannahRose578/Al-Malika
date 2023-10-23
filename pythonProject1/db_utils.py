import mysql.connector
from config import DATABASE_CONFIG

def connect_to_db():
    return mysql.connector.connect(**DATABASE_CONFIG)

def execute_query(connection, query, params=None):
    cursor = connection.cursor(dictionary=True)
    cursor.execute(query, params)
    result = cursor.fetchall()
    cursor.close()
    return result

def close_connection(connection):
    connection.close()
