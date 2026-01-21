#!/usr/bin/env python3
"""
Save a new note to the database.
Usage: python save_note.py "note content" [tag] [feel] [who] [todo]
"""

import sys
import os
import json

# Add the scripts directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from note_db import add_note, get_existing_tags, DB_PATH
from parse_note import parse_note

def save_note(content: str, tag: str = None, feel: str = None,
              who: str = None, todo: bool = False) -> dict:
    """
    Save a note to the database.

    Args:
        content: The note content
        tag: Optional tag
        feel: Optional feeling
        who: Optional person/mention
        todo: Whether this is a todo item

    Returns:
        Dictionary with the saved note data
    """
    existing_tags = get_existing_tags()

    # Parse the content to extract fields
    parsed = parse_note(content, existing_tags)

    # Use parsed values if not explicitly provided
    final_tag = tag or parsed["tag"]
    final_feel = feel or parsed["feel"]
    final_who = who or parsed["who"]
    final_todo = todo or parsed["todo"]
    clean_content = parsed["clean_content"]

    # Save to database
    result = add_note(clean_content, final_tag, final_feel, final_who, final_todo)

    return {
        "id": result["id"],
        "content": result["content"],
        "tag": result["tag"],
        "feel": result["feel"],
        "who": result["who"],
        "todo": result["todo"],
        "time": result["time"]
    }

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python save_note.py \"note content\"")
        sys.exit(1)

    content = sys.argv[1]

    result = save_note(content)

    print(json.dumps(result, ensure_ascii=False, indent=2))
