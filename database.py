import sqlite3

connection = sqlite3.connect("tasks.db") 
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NOT NULL,
description TEXT NOT NULL,
due_date TEXT NOT NULL, 
completed INTEGER
)""")