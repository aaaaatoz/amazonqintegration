import sqlite3

import os

DB_HOST = os.environ.get("DB_HOST")
DB_USER = os.environ.get("DB_USER")

def get_connection():
    conn = sqlite3.connect(f"{DB_HOST}/{DB_USER}")
    return conn

def fetch_user(user_id):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        return cursor.fetchone()
    finally:
        conn.close()
