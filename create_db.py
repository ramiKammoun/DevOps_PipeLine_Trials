import sqlite3

def connect_to_db(database):
    conn = sqlite3.connect(database)
    return conn

def create_db_table(database):
    try:
        conn = connect_to_db(database)
        conn.execute("DROP TABLE IF EXISTS books")
        conn.execute('''
            CREATE TABLE books (
                book_id INTEGER PRIMARY KEY NOT NULL,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                number TEXT NOT NULL,
            );
        ''')

        conn.commit()
        print("Book table created successfully")
    except:
        print("Book table creation failed - Maybe table")
    finally:
        conn.close()