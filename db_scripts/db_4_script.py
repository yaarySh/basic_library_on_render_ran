import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Add the Password column to the Users table
cursor.execute(
    """
    ALTER TABLE Users
    ADD COLUMN Password TEXT
"""
)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Password column added successfully.")
