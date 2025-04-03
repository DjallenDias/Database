import psycopg2
from src.config import DB_URL

def get_connection():
    try:
        conn = psycopg2.connect(DB_URL)
        return conn
    
    except Exception as e:
        print("Error while trying to connect to: {e}")
        return None