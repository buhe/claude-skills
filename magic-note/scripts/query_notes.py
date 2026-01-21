#!/usr/bin/env python3
"""
Query notes from the database.
"""

import sys
import os
import json

# Add the scripts directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from note_db import (
    get_notes_by_days,
    get_notes_with_feel_or_mention,
    get_notes_by_feel,
    get_notes_by_tag,
    get_all_notes
)

def query_notes_review(days: int) -> list:
    """Query notes that need review (have @ or $) from last N days."""
    return get_notes_with_feel_or_mention(days)

def query_notes_by_feel(feel: str, days: int = None) -> list:
    """Query notes by feeling."""
    return get_notes_by_feel(feel, days)

def query_notes_by_tag(tag: str, days: int = None) -> list:
    """Query notes by tag."""
    return get_notes_by_tag(tag, days)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Query notes from database')
    parser.add_argument('--review', type=int, help='Query notes needing review from last N days')
    parser.add_argument('--feel', type=str, help='Query by feeling')
    parser.add_argument('--tag', type=str, help='Query by tag')
    parser.add_argument('--days', type=int, help='Filter by last N days')

    args = parser.parse_args()

    if args.review:
        results = query_notes_review(args.review)
    elif args.feel:
        results = query_notes_by_feel(args.feel, args.days)
    elif args.tag:
        results = query_notes_by_tag(args.tag, args.days)
    else:
        print("Please specify --review, --feel, or --tag")
        sys.exit(1)

    print(json.dumps(results, ensure_ascii=False, indent=2))
