# External World: APIs & DBs

import sqlite3
# Note: 'requests' would be imported here for APIs

def database_demo():
    # SQLite: Built-in Database
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE buddies (name text, level integer)')
    cursor.execute('INSERT INTO buddies VALUES ("Jernish", 100)')
    
    conn.commit()
    cursor.execute('SELECT * FROM buddies')
    print(f"DB Result: {cursor.fetchone()}")
    conn.close()

if __name__ == "__main__":
    database_demo()
    print("\nPro-Tip: Use 'requests' library for Web APIs!")
