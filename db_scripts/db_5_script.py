import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Set a default password for all existing users
default_password = "defaultpassword"  # Change this as needed
cursor.execute(
    """
    UPDATE Users
    SET Password = ?
    WHERE Password IS NULL
""",
    (default_password,),
)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Passwords updated successfully.")
