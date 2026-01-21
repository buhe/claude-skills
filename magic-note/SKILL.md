---
name: magic-note
description: Intelligent note-taking and query system with tags (#tag), feelings ($feel), mentions (@who), and todo (&) support. Use when user wants to save/record notes with automatic field extraction, query notes by time/feeling/tag or review notes with feelings/mentions, or visualize relationships between notes using ASCII art. Commands include save/记录 xxx, 过去X天有什么note需要回顾, 过去X天有什么{feel}的note, 过去X个月的{tag} for relationship visualization.
---

# Magic Note

智能笔记记录与查询系统，支持标签、情感、人员和待办事项，以及笔记间关系的可视化。

## 数据库位置

- 配置文件路径: `/Users/guyanhua/.claude/note` （这是一个**文本文件**，里面存储 sqlite 数据库的路径）
- 首次使用时：
  1. 检查 `/Users/guyanhua/.claude/note` 是否存在
  2. 如果存在，读取其中的 sqlite 数据库路径
  3. 如果不存在，询问用户"请输入 SQLite 数据库的保存路径（如 `/Users/guyanhua/.claude/notes.sqlite`）"，然后将该路径写入配置文件

## 表结构

| 字段 | 类型 | 说明 |
|------|------|------|
| content | TEXT | 笔记内容 |
| tag | TEXT | 分类标签 (#tag) |
| feel | TEXT | 当时感觉 ($feel) |
| who | TEXT | 相关人/事 (@who) |
| todo | BOOLEAN | 是否为待办事项 (&) |
| time | TIMESTAMP | 记录时间 |

## 工作流程

### 1. 记录笔记

**触发词**: `save`, `记录`, `写下`, `添加笔记`

**语法格式**:
```
save/记录 [内容] [#标签] [$感觉] [@人/事] [&待办标记]
```

**示例**:
- `save 今天股票需要加仓，真恨呀` → 自动分析提取
- `记录 #股票 今天大盘大跌 $痛苦 @顾艳华`
- `save & 今天去买手纸`

**处理步骤**:
1. 检查 `/Users/guyanhua/.claude/note` 是否存在
   - 如果是文本文件，读取其中的 sqlite 路径
   - 如果不存在或为空：
     * 询问用户："请输入 SQLite 数据库的保存路径"（提供默认建议如 `/Users/guyanhua/.claude/notes.sqlite`）
     * 将用户选择的路径写入 `/Users/guyanhua/.claude/note` 文件
2. 调用 `scripts/save_note.py` 保存笔记
3. 自动解析内容提取 `tag`, `feel`, `who`, `todo`
4. **重要**: tag 只使用已有标签，不自由发挥；feel 和 who 可以自由发挥
5. 返回添加的字段（无论是显式指定还是自动分析）

**Python 脚本**:
```python
python3 scripts/save_note.py "笔记内容"
```

### 2. 查询笔记

#### 2.1 回顾笔记（含 @ 或 $）

**触发词**: `回顾`, `需要回顾`, `有什么note需要回顾`

**示例**: `过去1天有什么note需要回顾吗？`

**处理**: 查询含有 feel 或 who 的笔记

**Python 脚本**:
```python
python3 scripts/query_notes.py --review 1
```

#### 2.2 按感觉查询

**触发词**: `有什么{感觉}的note`, `过去X天{感觉}`

**示例**: `过去1天有什么兴奋的note`

**Python 脚本**:
```python
python3 scripts/query_notes.py --feel 兴奋 --days 1
```

#### 2.3 按标签查询

**触发词**: `过去X个月的{标签}`, `{标签}相关note`

**示例**: `过去一个月的股票笔记`

**Python 脚本**:
```python
python3 scripts/query_notes.py --tag 股票 --days 30
```

### 3. 关系可视化

**触发词**: `过去X个月的{tag}` 暗示需要关系图

**处理步骤**:
1. 获取指定时间范围内该 tag 的所有笔记
2. 使用 AI 分析笔记间的潜在关系（共同关键词、语义相似性、时间关联等）
3. 生成 ASCII 艺术图，笔记作为节点，有关联则连接

**ASCII 图示例**:
```
         阅读
         苹果的
xx       财报     xx
    │         │         │
    |         │         |
    研究苹果股票──────ios生态──────xx
    │         │         │
    │         |        │
    │         xx      │
    |          │        |
   xx──xx──xx
```

## 脚本说明

### scripts/note_db.py

数据库操作模块，提供以下函数:
- `init_db()` - 初始化数据库
- `add_note(content, tag, feel, who, todo)` - 添加笔记
- `get_existing_tags()` - 获取已有标签列表
- `get_notes_by_days(days)` - 获取N天内的笔记
- `get_notes_with_feel_or_mention(days)` - 获取含feel/who的笔记
- `get_notes_by_feel(feel, days)` - 按感觉查询
- `get_notes_by_tag(tag, days)` - 按标签查询

### scripts/parse_note.py

解析笔记内容，提取 tag/feel/who/todo:
```python
from parse_note import parse_note
parsed = parse_note("今天股票需要加仓 $兴奋", existing_tags)
# Returns: {"tag": "股票", "feel": "兴奋", "who": None, "todo": False, ...}
```

### scripts/save_note.py

保存笔记的主入口:
```bash
python3 scripts/save_note.py "笔记内容"
```

### scripts/query_notes.py

查询笔记的主入口:
```bash
# 回顾笔记
python3 scripts/query_notes.py --review 1

# 按感觉查询
python3 scripts/query_notes.py --feel 兴奋 --days 1

# 按标签查询
python3 scripts/query_notes.py --tag 股票 --days 30
```
