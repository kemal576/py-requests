import requests
from src.config import Settings
from src.exceptions.my_exception import MyException
from src.models.comment import Comment
from src.models.post import Post
from requests.exceptions import HTTPError

url = Settings.API_URL


class PostRequests:
    @staticmethod
    def get(post_id: int) -> Post:
        response = requests.get(f"{url}/posts/{post_id}")
        try:
            response.raise_for_status()
        except HTTPError:
            raise MyException(status=response.status_code)

        return Post(**response.json())

    @staticmethod
    def get_comments(post_id: int) -> list:
        response = requests.get(f"{url}/posts/{post_id}/comments")
        try:
            response.raise_for_status()
        except HTTPError:
            raise MyException(status=response.status_code)

        return [Comment(**comment) for comment in response.json()]

    @staticmethod
    def get_all() -> list:
        resp = requests.get(f"{url}/posts")
        return [Post(**post) for post in resp.json()]

    @staticmethod
    def create(post: Post) -> Post:
        resp = requests.post(f"{url}/posts", data=post.__dict__)
        if resp.status_code == 201:
            return Post(**resp.json())
        raise MyException(resp.status_code)

    @staticmethod
    def delete(post_id: int) -> str:
        resp = requests.delete(f"{url}/posts/{post_id}")
        if resp.status_code == 200:
            return "Delete successful."
        raise MyException(resp.status_code)

    @staticmethod
    def put(post_id: int, post: Post) -> Post:
        resp = requests.put(f"{url}/posts/{post_id}", data=post.__dict__)
        if resp.status_code == 200:
            return Post(**resp.json())
        raise MyException(resp.status_code)

    @staticmethod
    def patch(post_id: int, data: dict) -> Post:
        resp = requests.patch(f"{url}/posts/{post_id}", data=data)
        if resp.status_code == 200:
            return Post(**resp.json())
        raise MyException(resp.status_code)
