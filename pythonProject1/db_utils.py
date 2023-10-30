import pymysql
from config import DB_CONFIG

def get_db_connection():
    try:
        connection = pymysql.connect(**DB_CONFIG)
        return connection
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
