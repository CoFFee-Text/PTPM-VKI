from src.commentsDb import DatabaseRepository
from src.forumParser import ForumParser

if __name__ == "__main__":
    url = "https://habr.com/ru/companies/ruvds/articles/729124/comments/"

    repo = DatabaseRepository("comments.db")
    parser = ForumParser()

    comments = parser.parse_page(url)
    print(f"Найдено комментариев: {len(comments)}")

    parser.save_to_db(comments, repo)

    all_rows = repo.cursor.execute("SELECT id, name, substr(message, 1, 8096) FROM comments").fetchall()
    for row in all_rows:
        print(dict(row))

    repo.close()
