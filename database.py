import sqlite3

conn = sqlite3.connect("tarot.db")
cursor = conn.cursor()

def init_db():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        first_name TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS card_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        card_name TEXT,
        date TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS monthly_energy (
        user_id INTEGER,
        month TEXT,
        card_name TEXT,
        PRIMARY KEY (user_id, month)
    )
    """)

    conn.commit()

def add_user(user_id, username, first_name):
    cursor.execute("""
    INSERT OR IGNORE INTO users (id, username, first_name)
    VALUES (?, ?, ?)
    """, (user_id, username, first_name))
    conn.commit()

def save_card(user_id, card_name, date):
    cursor.execute("""
    INSERT INTO card_history (user_id, card_name, date)
    VALUES (?, ?, ?)
    """, (user_id, card_name, date))
    conn.commit()

def get_card_count(user_id, card_name):
    cursor.execute("""
    SELECT COUNT(*) FROM card_history
    WHERE user_id = ? AND card_name = ?
    """, (user_id, card_name))
    return cursor.fetchone()[0]

def get_top_card(user_id):
    cursor.execute("""
    SELECT card_name, COUNT(card_name) as count
    FROM card_history
    WHERE user_id = ?
    GROUP BY card_name
    ORDER BY count DESC
    LIMIT 1
    """, (user_id,))
    return cursor.fetchone()

def get_monthly_energy(user_id, month):
    cursor.execute("""
    SELECT card_name FROM monthly_energy
    WHERE user_id = ? AND month = ?
    """, (user_id, month))
    return cursor.fetchone()

def save_monthly_energy(user_id, month, card_name):
    cursor.execute("""
    INSERT OR REPLACE INTO monthly_energy (user_id, month, card_name)
    VALUES (?, ?, ?)
    """, (user_id, month, card_name))
    conn.commit()