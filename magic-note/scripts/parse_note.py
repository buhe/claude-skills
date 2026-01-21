#!/usr/bin/env python3
"""
Parse note content to extract tags, feelings, people, and todo status.
"""

import re
from typing import Dict, Optional, List

def parse_note(content: str, existing_tags: List[str]) -> Dict[str, any]:
    """
    Parse note content to extract tags, feelings, people, and todo status.

    Args:
        content: The note content to parse
        existing_tags: List of existing tags to match against

    Returns:
        Dictionary with extracted fields: tag, feel, who, todo, clean_content
    """
    result = {
        "tag": None,
        "feel": None,
        "who": None,
        "todo": False,
        "clean_content": content
    }

    # Extract tags (#tag)
    tag_pattern = r'#(\S+)'
    tags = re.findall(tag_pattern, content)
    if tags:
        # Use existing tags if matched, otherwise use first found tag
        for t in tags:
            if t in existing_tags:
                result["tag"] = t
                break
        if not result["tag"]:
            result["tag"] = tags[0]
        # Remove tags from clean content
        content = re.sub(tag_pattern, '', content).strip()

    # Extract feelings ($feel)
    feel_pattern = r'\$(\S+)'
    feels = re.findall(feel_pattern, content)
    if feels:
        result["feel"] = feels[0]
        # Remove feelings from clean content
        content = re.sub(feel_pattern, '', content).strip()

    # Extract people/mentions (@who)
    who_pattern = r'@(\S+)'
    whos = re.findall(who_pattern, content)
    if whos:
        result["who"] = ", ".join(whos)
        # Remove mentions from clean content
        content = re.sub(who_pattern, '', content).strip()

    # Extract todo (& indicates todo item)
    if '&' in content:
        result["todo"] = True
        # Remove & from clean content
        content = content.replace('&', '').strip()

    result["clean_content"] = content

    return result

if __name__ == "__main__":
    # Test examples
    existing_tags = ["股票", "工作", "生活"]

    test_notes = [
        "今天股票需要加仓，真恨呀",
        "#股票 今天需要加仓 $兴奋 @顾艳华",
        "& 今天去买手纸",
        "过去1天有什么note需要回顾吗",
        "$痛苦 今天工作很累 @老板",
    ]

    for note in test_notes:
        parsed = parse_note(note, existing_tags)
        print(f"Original: {note}")
        print(f"Parsed: {parsed}")
        print()
