import sqlite3
from contextlib import contextmanager
import logging
import os
import sys

# Add the project root to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from config import DATABASE_NAME

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@contextmanager
def get_db_connection():
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        yield conn
    except sqlite3.Error as e:
        logger.error(f"Database error: {e}")
        raise
    finally:
        if conn:
            conn.close()

def init_db():
    with get_db_connection() as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS daily_logs
                     (id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT, mood REAL, serenity REAL, sleep REAL, productivity REAL, enjoyment REAL, notes TEXT)''')
        c.execute('''CREATE TABLE IF NOT EXISTS chat_history
                     (id INTEGER PRIMARY KEY AUTOINCREMENT, role TEXT, content TEXT)''')
        conn.commit()

def insert_daily_log(date, mood, serenity, sleep, productivity, enjoyment, notes):
    with get_db_connection() as conn:
        c = conn.cursor()
        c.execute("INSERT INTO daily_logs (date, mood, serenity, sleep, productivity, enjoyment, notes) VALUES (?, ?, ?, ?, ?, ?, ?)",
                  (date, mood, serenity, sleep, productivity, enjoyment, notes))
        conn.commit()

def get_all_daily_logs():
    with get_db_connection() as conn:
        return conn.execute("SELECT * FROM daily_logs").fetchall()

def insert_chat_message(role, content):
    with get_db_connection() as conn:
        c = conn.cursor()
        c.execute("INSERT INTO chat_history (role, content) VALUES (?, ?)", (role, content))
        conn.commit()

def get_chat_history():
    with get_db_connection() as conn:
        return conn.execute("SELECT * FROM chat_history").fetchall()

def clear_chat_history():
    with get_db_connection() as conn:
        c = conn.cursor()
        c.execute("DELETE FROM chat_history")
        conn.commit()

def delete_all_data():
    with get_db_connection() as conn:
        c = conn.cursor()
        c.execute("DELETE FROM daily_logs")
        c.execute("DELETE FROM chat_history")
        conn.commit()