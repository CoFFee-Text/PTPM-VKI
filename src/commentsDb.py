import sqlite3

class DatabaseRepository:
    def __init__(self, db_path='comments.db'):
        self.connection = sqlite3.connect(db_path)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS comments (
                id integer primary key,
                name text CHECK(length(name) <= 256) not null,
                message TEXT CHECK(length(message) <= 8096) not null
            )
        ''')
        self.connection.commit()

    def get_by_id(self, comment_id: int) -> dict | None:
        self.cursor.execute(
            "SELECT id, name, message FROM comments WHERE id = ?",
            (comment_id,)
        )
        row = self.cursor.fetchone()
        return dict(row) if row else None

    def get_by_name(self, username: str) -> list[dict]:
        self.cursor.execute(
            "SELECT id, name, message FROM comments WHERE name = ?",
            (username,)
        )
        rows = self.cursor.fetchall()
        return [dict(row) for row in rows]

    def add(self, comment_id: int, username: str, message: str) -> bool:
        if not isinstance(comment_id, int) or isinstance(comment_id, bool):
            raise TypeError("comment_id должен быть целым числом")
        if not isinstance(username, str) or not isinstance(message, str):
            raise TypeError("username и message должны быть строками")
        if not username.strip():
            raise ValueError("username не может быть пустым")
        if not message.strip():
            raise ValueError("message не может быть пустым")
        if len(username) > 256:
            raise ValueError("Длина username не должна превышать 256 символов")
        if len(message) > 8096:
            raise ValueError("Длина message не должна превышать 8096 символов")

        self.cursor.execute(
            "INSERT INTO comments (id, name, message) VALUES (?, ?, ?)",
            (comment_id, username, message)
        )
        self.connection.commit()
        return True

    def update(self, comment_id: int, new_message: str) -> bool:
        if not isinstance(comment_id, int) or isinstance(comment_id, bool):
            raise TypeError("comment_id должен быть целым числом")
        if not isinstance(new_message, str):
            raise TypeError("new_message должен быть строкой")
        if not new_message.strip():
            raise ValueError("message не может быть пустым")
        if len(new_message) > 8096:
            raise ValueError("Длина new_message не должна превышать 8096 символов")

        self.cursor.execute(
            "UPDATE comments SET message = ? WHERE id = ?",
            (new_message, comment_id)
        )
        self.connection.commit()
        return self.cursor.rowcount > 0

    def delete(self, comment_id: int) -> bool:
        self.cursor.execute(
            "DELETE FROM comments WHERE id = ?",
            (comment_id,)
        )
        self.connection.commit()
        return self.cursor.rowcount > 0

    def close(self):
        self.connection.close()