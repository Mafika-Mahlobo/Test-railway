import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def get_DBconnection():
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            port=os.getenv("DB_PORT", 37708)
        )
        if conn.is_connected():
            return conn
    except Exception as e:
        return f"DB connection error: {e}"
    return None
