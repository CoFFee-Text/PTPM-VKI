import sqlite3

class TriangleDB:
    def __init__(self, db_path='triangle.db'):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS triangle (
                Side1 REAL NOT NULL,
                Side2 REAL NOT NULL,
                Side3 REAL NOT NULL,
                Triangle_Type TEXT NOT NULL,
                Error_Message TEXT,
                PRIMARY KEY (Side1, Side2, Side3)
            )
        ''')
        self.connection.commit()

    def add(self, a, b, c, triangle_type, error_message=None):
        self.cursor.execute(
            "INSERT OR REPLACE INTO triangle VALUES (?, ?, ?, ?, ?)",
            (a, b, c, triangle_type, error_message)
        )
        self.connection.commit()

    def get(self, a, b, c) -> tuple[str, str | None] | None:
        self.cursor.execute(
            "SELECT Triangle_Type, Error_Message FROM triangle WHERE Side1=? AND Side2=? AND Side3=?",
            (a, b, c)
        )
        row = self.cursor.fetchone()
        return (row[0], row[1]) if row else None

    def delete(self, a, b, c):
        self.cursor.execute(
            "DELETE FROM triangle WHERE Side1=? AND Side2=? AND Side3=?",
            (a, b, c)
        )
        self.connection.commit()

    def close(self):
        self.connection.close()