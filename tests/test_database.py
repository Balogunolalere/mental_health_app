import pytest
from app.database import init_db, insert_daily_log, get_all_daily_logs, insert_chat_message, get_chat_history, clear_chat_history, delete_all_data
import sqlite3

@pytest.fixture(scope="module")
def test_db():
    conn = sqlite3.connect(':memory:')
    init_db()
    yield conn
    conn.close()

def test_insert_and_get_daily_log(test_db):
    insert_daily_log("2023-01-01", 7.5, 8.0, 6.5, 7.0, 8.5, "Test note")
    logs = get_all_daily_logs()
    assert len(logs) == 1
    assert logs[0][1:] == ("2023-01-01", 7.5, 8.0, 6.5, 7.0, 8.5, "Test note")

def test_insert_and_get_chat_message(test_db):
    insert_chat_message("user", "Test message")
    history = get_chat_history()
    assert len(history) == 1
    assert history[0][1:] == ("user", "Test message")

def test_clear_chat_history(test_db):
    insert_chat_message("user", "Test message 1")
    insert_chat_message("assistant", "Test message 2")
    clear_chat_history()
    history = get_chat_history()
    assert len(history) == 0

def test_delete_all_data(test_db):
    insert_daily_log("2023-01-01", 7.5, 8.0, 6.5, 7.0, 8.5, "Test note")
    insert_chat_message("user", "Test message")
    delete_all_data()
    logs = get_all_daily_logs()
    history = get_chat_history()
    assert len(logs) == 0
    assert len(history) == 0