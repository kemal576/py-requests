from dataclasses import dataclass


@dataclass
class Comment:
    id: int
    postId: int
    name: str
    email: str
    body: str

