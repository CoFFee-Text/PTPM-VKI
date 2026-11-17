import requests
from bs4 import BeautifulSoup
from src.commentsDb import DatabaseRepository

class ForumParser:
    def __init__(self):
        self.headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            )
        }

    def fetch_html(self, url: str) -> str:
        target_url = url if url.rstrip("/").endswith("/comments") else f"{url.rstrip('/')}/comments/"
        response = requests.get(target_url, headers=self.headers, timeout=30)
        response.raise_for_status()
        return response.text

    def parse_html(self, html: str) -> list[dict]:
        soup = BeautifulSoup(html, "lxml")
        parsed_comments = []
        comment_blocks = soup.find_all("article", class_="tm-comment-thread__comment")
        for block in comment_blocks:
            anchor = block.find(id=lambda x: x and x.startswith("comment_"))
            if not anchor:
                continue
            comment_id = int(anchor.get("id").replace("comment_", ""))

            author_tag = block.find("a", class_="tm-user-info__username")
            username = author_tag.get_text(strip=True) if author_tag else "Unknown"

            message_tag = block.find("div", class_="tm-comment__body-content")
            if not message_tag:
                continue
            message_html = message_tag.decode_contents().strip()

            parsed_comments.append({
                "id": comment_id,
                "name": username,
                "message": message_html
            })
        return parsed_comments

    def parse_page(self, url: str) -> list[dict]:
        return self.parse_html(self.fetch_html(url))

    def save_to_db(self, parsed_data: list[dict], repository: DatabaseRepository):
        for item in parsed_data:
            clean_message = item["message"][:8096]
            clean_name = item["name"][:256]

            if repository.get_by_id(item["id"]) is None:
                repository.add(
                    comment_id=item["id"],
                    username=clean_name,
                    message=clean_message
                )

    # def parse_page(self, url: str) -> list[dict]:
    #     target_url = url if url.rstrip("/").endswith("/comments") else f"{url.rstrip('/')}/comments/"
    #
    #     response = requests.get(target_url, headers=self.headers, timeout=30)
    #     response.raise_for_status()
    #
    #     soup = BeautifulSoup(response.text, "lxml")
    #     parsed_comments = []
    #
    #     comment_blocks = soup.find_all("article", class_="tm-comment-thread__comment")
    #
    #     for block in comment_blocks:
    #         anchor = block.find(id=lambda x: x and x.startswith("comment_"))
    #         if not anchor:
    #             continue
    #         comment_id = int(anchor.get("id").replace("comment_", ""))
    #
    #         author_tag = block.find("a", class_="tm-user-info__username")
    #         username = author_tag.get_text(strip=True) if author_tag else "Unknown"
    #
    #         message_tag = block.find("div", class_="tm-comment__body-content")
    #         if not message_tag:
    #             continue
    #         message_html = message_tag.decode_contents().strip()
    #
    #         parsed_comments.append({
    #             "id": comment_id,
    #             "name": username,
    #             "message": message_html
    #         })
    #
    #     return parsed_comments
    #
    # def save_to_db(self, parsed_data: list[dict], repository: DatabaseRepository) -> int:
    #     for item in parsed_data:
    #         clean_message = item["message"][:8096]
    #         clean_name = item["name"][:256]
    #
    #         if repository.get_by_id(item["id"]) is None:
    #             repository.add(
    #                 comment_id=item["id"],
    #                 username=clean_name,
    #                 message=clean_message
    #             )