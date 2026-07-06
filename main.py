import sqlite3
import pandas as pd

conn = sqlite3.connect('tasks.sqlite') # create a database connection

cur = conn.cursor() # create a cursor object to execute SQL commands

cur.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY UNIQUE,   
    title TEXT NOT NULL,
    description TEXT,
    completed BOOLEAN NOT NULL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    
    );""") # create table if it does not exist

cur.execute("DELETE FROM tasks") # clear the table before inserting new data

cur.execute('''
INSERT INTO tasks (title, completed) VALUES
            ('Fix login Bug', 0),
            ('Write unit tests', 0),
            ('Deploy to Staging', 1),
            ('Update README', 0),
            ('Code review PR #42', 1) 
''')  # insert sample data

conn.commit() # commit the changes to the database

df = pd.read_sql_query("SELECT * FROM tasks", conn) # read the data from the database into a pandas DataFrame
columns=['id', 'title','completed',] # select only the columns we want to keep
df = df[columns] # filter the DataFrame to include only the selected columns


print(df) # print the DataFrame to the console

conn.close() # close the database connection


