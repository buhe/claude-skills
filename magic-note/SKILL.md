---
name: magic-note
description: Intelligent note-taking and query system with tags (#tag), feelings ($feel), mentions (@who), and todo (&) support. Use when user wants to save/record notes with automatic field extraction, query notes by time/feeling/tag or review notes with feelings/mentions, or visualize relationships between notes using ASCII art. Commands include save/record xxx, review notes from past X days, notes with {feel} from past X days, {tag} notes from past X months for relationship visualization.
---

# Magic Note

Intelligent note-taking and query system supporting tags, feelings, mentions, todos, and relationship visualization between notes.

## Database Location

- Config file path: `/Users/guyanhua/.claude/note` (This is a **text file** storing the sqlite database path)
- First-time setup:
  1. Check if `/Users/guyanhua/.claude/note` exists
  2. If it exists, read the sqlite database path from it
  3. If it doesn't exist, ask user "Please enter SQLite database save path (e.g., `/Users/guyanhua/.claude/notes.sqlite`)" and write that path to the config file

## Table Structure

| Field | Type | Description |
|-------|------|-------------|
| content | TEXT | Note content |
| tag | TEXT | Category tag (#tag) |
| feel | TEXT | Feeling at the time ($feel) |
| who | TEXT | Related person/thing (@who) |
| todo | BOOLEAN | Is this a todo item (&) |
| time | TIMESTAMP | Record time |

## Workflow

### 1. Save Notes

**Trigger words**: `save`, `record`, `write`, `add note`

**Syntax**:
```
save/record [content] [#tag] [$feel] [@who] [&todo]
```

**Examples**:
- `save Need to add more stock positions today` → Auto-analyze and extract
- `record #stock Market crashed today $pain @guyanhua`
- `save & Buy toilet paper today`

**Processing steps**:
1. Check if `/Users/guyanhua/.claude/note` exists
   - If it's a text file, read the sqlite path from it
   - If it doesn't exist or is empty:
     * Ask user: "Please enter SQLite database save path" (provide default suggestion like `/Users/guyanhua/.claude/notes.sqlite`)
     * Write user's chosen path to `/Users/guyanhua/.claude/note` file
2. Call `scripts/save_note.py` to save the note
3. Automatically parse content to extract `tag`, `feel`, `who`, `todo`
4. **Important**: tag only uses existing tags; feel and who can be freely created
5. Return extracted fields (whether explicitly specified or auto-analyzed)

**Python script**:
```python
python3 scripts/save_note.py "note content"
```

### 2. Query Notes

#### 2.1 Review Notes (containing @ or $)

**Trigger words**: `review`, `need review`, `notes to review`

**Example**: `What notes need review from past 1 day?`

**Processing**: Query notes containing feel or who

**Python script**:
```python
python3 scripts/query_notes.py --review 1
```

#### 2.2 Query by Feeling

**Trigger words**: `notes with {feel}`, `{feel} notes from past X days`

**Example**: `Any excited notes from past 1 day`

**Python script**:
```python
python3 scripts/query_notes.py --feel excited --days 1
```

#### 2.3 Query by Tag

**Trigger words**: `{tag} notes from past X months`, `{tag} related notes`

**Example**: `Stock notes from past month`

**Python script**:
```python
python3 scripts/query_notes.py --tag stock --days 30
```

### 3. Relationship Visualization

**Trigger words**: `{tag} from past X months` implies need for relationship graph

**Processing steps**:
1. Get all notes for that tag within the specified time range
2. Use AI to analyze potential relationships between notes (common keywords, semantic similarity, time correlation, etc.)
3. Generate ASCII art graph with notes as nodes, connected if related

**ASCII graph example**:
```
         Read
        Apple's
xx       report     xx
    |         |         |
    |         |         |
    Study Apple stock────ios ecosystem────xx
    |         |         |
    |         |        |
    |         xx      |
    |          |        |
   xx──xx──xx
```

## Script Documentation

### scripts/note_db.py

Database operation module, providing the following functions:
- `init_db()` - Initialize database
- `add_note(content, tag, feel, who, todo)` - Add note
- `get_existing_tags()` - Get list of existing tags
- `get_notes_by_days(days)` - Get notes from N days
- `get_notes_with_feel_or_mention(days)` - Get notes containing feel/who
- `get_notes_by_feel(feel, days)` - Query by feeling
- `get_notes_by_tag(tag, days)` - Query by tag

### scripts/parse_note.py

Parse note content to extract tag/feel/who/todo:
```python
from parse_note import parse_note
parsed = parse_note("Need to add stock today $excited", existing_tags)
# Returns: {"tag": "stock", "feel": "excited", "who": None, "todo": False, ...}
```

### scripts/save_note.py

Main entry point for saving notes:
```bash
python3 scripts/save_note.py "note content"
```

### scripts/query_notes.py

Main entry point for querying notes:
```bash
# Review notes (notes with @ or $ from past N days)
python3 scripts/query_notes.py --review 1

# Query by feeling
python3 scripts/query_notes.py --feel excited --days 1

# Query by tag
python3 scripts/query_notes.py --tag stock --days 30

# Query ALL notes from past N days
python3 scripts/query_notes.py --all 30
```

**IMPORTANT**: `--all N` means "query all notes from past N days", NOT "query all notes ever".
- `--all 1` → past 1 day only
- `--all 30` → past 30 days
- Do NOT use `--all 1 --days 30` together (the `--all` parameter already specifies the days)
