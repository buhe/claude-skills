#!/usr/bin/env python3
"""
Magic Note Database Operations

Manages SQLite database for storing notes with tags, feelings, people, and todos.
Database location: /Users/guyanhua/.claude/note
"""

import sqlite3
import json
import os
from datetime import datetime
from typing import Optional, List, Dict, Any

# Configuration file that stores the sqlite database path
PREF_FILE = "/Users/guyanhua/.claude/note"

# Check if note path preference file exists
if os.path.exists(PREF_FILE) and os.path.isfile(PREF_FILE):
    try:
        with open(PREF_FILE, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            if content:
                DB_PATH = content
            else:
                DB_PATH = None  # Empty file, needs setup
    except (UnicodeDecodeError, IOError):
        # If the pref file is not readable as text, needs setup
        DB_PATH = None
else:
    # Pref file doesn't exist yet
    DB_PATH = None

def get_db_connection():
    """Get a connection to the notes database."""
    if DB_PATH is None:
        raise FileNotFoundError(
            f"数据库未配置。\n"
            f"配置文件 '{PREF_FILE}' 不存在或为空。\n"
            f"请先创建该文件并写入 SQLite 数据库的路径，例如：\n"
            f"  echo '/Users/guyanhua/.claude/notes.sqlite' > {PREF_FILE}"
        )
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize the database with the notes table."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            tag TEXT,
            feel TEXT,
            who TEXT,
            todo BOOLEAN DEFAULT 0,
            time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()

def add_note(content: str, tag: Optional[str] = None, feel: Optional[str] = None,
             who: Optional[str] = None, todo: bool = False) -> Dict[str, Any]:
    """Add a new note to the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO notes (content, tag, feel, who, todo, time)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (content, tag, feel, who, 1 if todo else 0, datetime.now().isoformat()))

    note_id = cursor.lastrowid
    conn.commit()
    conn.close()

    return {
        "id": note_id,
        "content": content,
        "tag": tag,
        "feel": feel,
        "who": who,
        "todo": todo,
        "time": datetime.now().isoformat()
    }

def get_existing_tags() -> List[str]:
    """Get list of existing tags in the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT DISTINCT tag FROM notes WHERE tag IS NOT NULL')
    rows = cursor.fetchall()
    conn.close()

    return [row[0] for row in rows]

def get_notes_by_days(days: int) -> List[Dict[str, Any]]:
    """Get notes from the last N days."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM notes
        WHERE datetime(time) >= datetime('now', '-' || ? || ' days')
        ORDER BY time DESC
    ''', (days,))

    rows = cursor.fetchall()
    conn.close()

    return [dict(row) for row in rows]

def get_notes_with_feel_or_mention(days: int) -> List[Dict[str, Any]]:
    """Get notes that have feelings (@) or mentions ($) from the last N days."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM notes
        WHERE datetime(time) >= datetime('now', '-' || ? || ' days')
        AND (feel IS NOT NULL OR who IS NOT NULL OR todo = 1)
        ORDER BY time DESC
    ''', (days,))

    rows = cursor.fetchall()
    conn.close()

    return [dict(row) for row in rows]

def get_notes_by_feel(feel: str, days: Optional[int] = None) -> List[Dict[str, Any]]:
    """Get notes by feeling, optionally filtered by days."""
    conn = get_db_connection()
    cursor = conn.cursor()

    if days:
        cursor.execute('''
            SELECT * FROM notes
            WHERE feel = ? AND datetime(time) >= datetime('now', '-' || ? || ' days')
            ORDER BY time DESC
        ''', (feel, days))
    else:
        cursor.execute('''
            SELECT * FROM notes WHERE feel = ? ORDER BY time DESC
        ''', (feel,))

    rows = cursor.fetchall()
    conn.close()

    return [dict(row) for row in rows]

def get_notes_by_tag(tag: str, days: Optional[int] = None) -> List[Dict[str, Any]]:
    """Get notes by tag, optionally filtered by days."""
    conn = get_db_connection()
    cursor = conn.cursor()

    if days:
        cursor.execute('''
            SELECT * FROM notes
            WHERE tag = ? AND datetime(time) >= datetime('now', '-' || ? || ' days')
            ORDER BY time DESC
        ''', (tag, days))
    else:
        cursor.execute('''
            SELECT * FROM notes WHERE tag = ? ORDER BY time DESC
        ''', (tag,))

    rows = cursor.fetchall()
    conn.close()

    return [dict(row) for row in rows]

def get_all_notes() -> List[Dict[str, Any]]:
    """Get all notes from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM notes ORDER BY time DESC')
    rows = cursor.fetchall()
    conn.close()

    return [dict(row) for row in rows]

# Initialize DB on import
if __name__ == "__main__":
    init_db()
    print(f"Database initialized at: {DB_PATH}")
else:
    # Initialize when module is imported
    init_db()
