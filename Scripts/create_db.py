import sqlite3
import os

# Path to the SQLite database file
db_path = os.path.join(os.path.dirname(__file__), 'leetcode_streak.db')

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create a table to store streak data
cursor.execute('''
CREATE TABLE IF NOT EXISTS streak (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    last_login_date TEXT NOT NULL,
    current_streak INTEGER DEFAULT 0
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database and table created successfully!")