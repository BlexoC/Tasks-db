import sqlite3
import pandas as pd

conn = sqlite3.connect('tasks.sqlite')

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,   
    title TEXT NOT NULL,
    description TEXT,
    completed BOOLEAN NOT NULL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    
    );""")

cur.execute("DELETE FROM tasks")

cur.execute('''
INSERT INTO tasks (title, completed) VALUES
            ('Fix login Bug', 0),
            ('Write unit tests', 0),
            ('Deploy to Staging', 1),
            ('Update README', 0),
            ('Code review PR #42', 1)
''')

conn.commit()

df = pd.read_sql_query("SELECT * FROM tasks", conn)
columns=['id', 'title','completed',]
df = df[columns]


print(df)

conn.close()


