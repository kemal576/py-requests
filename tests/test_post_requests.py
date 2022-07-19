from src.exceptions.my_exception import MyException
from src.models.comment import Comment
from src.models.post import Post
from src.my_requests.post_requests import PostRequests


def test_get_post_success():
    post = PostRequests.get(1)
    assert type(post) is Post
    assert post.id == 1


def test_get_post_fail():
    try:
        post = PostRequests.get(0)
    except MyException as e:
        assert e.status == 404


def test_get_comments_success():
    comments: list[Comment] = PostRequests.get_comments(1)
    assert comments[0].postId == 1


def test_get_comments_fail():
    try:
        comments = PostRequests.get_comments(0)
    except MyException as e:
        assert e.status == 404


def test_get_all_success():
    posts: list[Post] = PostRequests.get_all()
    assert len(posts) > 0


def test_create_post_success():
    post = Post(0, 1, "test title", "test body")
    new_post = PostRequests.create(post)

    assert new_post.id > 0
    assert new_post.userId == "1"
    assert new_post.title == "test title"
    assert new_post.body == "test body"


def test_put_post_success():
    post = Post(1, 2, "test title put", "test body")
    updated_post = PostRequests.put(1, post)

    assert updated_post.userId == "2"
    assert updated_post.title == "test title put"


def test_put_post_fail():
    post = Post(2, 1, "test title put", "test body")

    try:
        updated_post = PostRequests.put(0, post)
    except MyException as e:
        assert e.status == 500


def test_patch_post_success():
    updated_post = PostRequests.patch(1, {"title": "patched title"})

    assert updated_post.userId == 1
    assert updated_post.title == "patched title"
