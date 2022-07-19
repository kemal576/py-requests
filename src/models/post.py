from dataclasses import dataclass


@dataclass
class Post:
    id: int
    userId: int
    title: str
    body: str

