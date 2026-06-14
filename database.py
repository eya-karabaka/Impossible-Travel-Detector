import sqlite3

DB_PATH = "database.db" 
def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row 
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor() 
    cursor.execute("""                           
        CREATE TABLE IF NOT EXISTS logins (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            user TEXT NOT NULL,
            ip TEXT NOT NULL,
            city TEXT NOT NULL,
            lat REAL NOT NULL,
            lon REAL NOT NULL,
            timestamp TEXT NOT NULL
        )
    """) 
    conn.commit() 
    conn.close() 

def get_all_logins():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM logins")
    rows = cursor.fetchall() 
    conn.close()
    return [dict(row) for row in rows]

def insert_login(user, ip, city, lat, lon, timestamp):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO logins (user, ip, city, lat, lon, timestamp)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (user, ip, city, lat, lon, timestamp))
    conn.commit()
    conn.close()
  