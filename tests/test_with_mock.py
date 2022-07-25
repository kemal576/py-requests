from src.exceptions.my_exception import MyException
from src.models.post import Post
from src.my_requests.post_requests import PostRequests


def test_get_post(mocker):
    mock = mocker.patch("src.my_requests.post_requests.requests.get")
    mock.return_value.status_code = 200
    mock.return_value.json.return_value = {
      "userId": 1,
      "id": 1,
      "title": "title mock test",
      "body": "event architect"
    }

    post = PostRequests.get(1)
    assert type(post) is Post
    assert post.id == 1
    assert post.title == "title mock test"


# def test_get_post_fail(mocker):
#     mock = mocker.patch("src.my_requests.post_requests.requests.get")
#     mock.return_value.status_code = 404
#
#     try:
#         post = PostRequests.get(0)
#     except MyException as e:
#         assert e.status == 404


def test_create_post(mocker):
    mock = mocker.patch("src.my_requests.post_requests.requests.post")
    mock.return_value.status_code = 201
    mock.return_value.json.return_value = {"id": 1, "userId": 1, "title": "test title", "body": "test body"}

    post = Post(0, 1, "test title", "test body")
    new_post = PostRequests.create(post)

    assert new_post.id > 0
    assert new_post.userId == 1
    assert new_post.title == "test title"
    assert new_post.body == "test body"


def test_put_post_success(mocker):
    post = Post(1, 2, "test title put", "test")
    mock = mocker.patch("src.my_requests.post_requests.requests.put")
    mock.return_value.status_code = 200
    mock.return_value.json.return_value = {"id": 1, "userId": 2, "title": "test title put", "body": "test"}

    updated_post = PostRequests.put(1, post)

    assert updated_post.userId == 2
    assert updated_post.title == "test title put"


def test_patch_post_success(mocker):
    mock = mocker.patch("src.my_requests.post_requests.requests.patch")
    mock.return_value.status_code = 200
    mock.return_value.json.return_value = {"id": 1, "userId": 1, "title": "patched title", "body": "test"}

    updated_post = PostRequests.patch(1, {"title": "patched title"})

    assert updated_post.id == 1
    assert updated_post.title == "patched title"
