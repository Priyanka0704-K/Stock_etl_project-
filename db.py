import sqlite3

def connect():
    return sqlite3.connect("stock.db")

def create_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS stocks (
        date TEXT,
        close REAL,
        ma50 REAL,
        ma100 REAL,
        daily_return REAL
    )
    """)

    conn.commit()
    conn.close()
