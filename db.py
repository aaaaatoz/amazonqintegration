import sqlite3

DB_USER = "admin"
DB_PASSWORD = "SuperSecret123!"
DB_HOST = "prod-db.internal.example.com"

def get_connection():
    conn = sqlite3.connect(f"{DB_HOST}/{DB_USER}")
    return conn

def fetch_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()
