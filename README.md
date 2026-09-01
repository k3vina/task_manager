# Task Manager (SQLite + OOP)

A command-line to-do list application built with Python, using object-oriented
principles and SQLite for persistent storage.

## Features

- Add tasks with a title, description, and due date
- View all tasks in a clean, aligned table format
- Mark tasks as complete
- Delete tasks
- Asks user to enter the priority of the task
- Tasks persist across runs using an SQLite database (`tasks.db`)

## Project Structure

```
task_manager/
├── task.py        # Task class — represents a single task
├── database.py     # TaskDatabase class — handles all SQLite CRUD operations
├── main.py         # CLI entry point — menu loop tying everything together
└── tasks.db        # SQLite database file (created automatically on first run)
```

## Requirements

- Python 3.x
- No external packages required — uses only the standard library
  (`sqlite3`, `datetime`)

## Installation
Clone this repository:
```bash
git clone https://github.com/k3vina/task_manager
dc task_manager
```

## How to Run

```bash
python main.py
```

You'll see a menu with the following options:

```
Add task
View task
Mark complete
Delete
Exit
```

Type an option exactly as shown to select it.

## Usage

**Add task** — prompts for a title and description; the due date is
generated automatically.

**View task** — displays all saved tasks in a table with columns for ID,
Title, Description, Due Date, Completed status, and Priority.

**Mark complete** — prompts for a task's ID and marks it as completed (`1`).

**Delete** — prompts for a task's ID and removes it from the database.

**Exit** — closes the database connection and ends the program.

## Design Notes

- `Task` (in `task.py`) is a plain data class: it stores a task's fields and
  knows how to display itself (`display_info()`) or format itself as a table
  row (`to_row()` / `header_row()`). It has no knowledge of the database.
- `TaskDatabase` (in `database.py`) owns all SQL logic. It receives an
  existing `sqlite3` connection from `main.py` rather than creating its own,
  so the connection's lifecycle (open → use → close) is controlled entirely
  by the caller.
- `main.py` is the only file that talks directly to the user — it collects
  input, builds `Task` objects, and calls methods on `TaskDatabase` to
  persist changes. It never writes raw SQL itself.
- Task IDs are auto-assigned by SQLite (`AUTOINCREMENT`) and are not
  reused after deletion. The "View task" table displays IDs as stored in
  the database, which may have gaps after deletions — this is intentional,
  since IDs are meant to be stable references, not a running count.

## Possible Extensions

- Category filtering
- Export task list to CSV
