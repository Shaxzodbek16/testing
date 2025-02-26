import pytest


@pytest.fixture(scope="session")
def mock_user_data():
    print("\nSession scope fixture was opened")
    users = {
        "user1": {"id": 1, "username": "alice", "email": "alice@gmail.com", "age": 15},
        "user2": {"id": 2, "username": "bob", "email": "bob@example.com", "age": 25},
    }
    yield users
    print("\nSession scope fixture was closed")


@pytest.fixture(scope="function")
def get_user(mock_user_data):
    def _get_user(user_key):
        return mock_user_data[user_key]

    return _get_user


def test_user_alice(get_user):
    user = get_user("user1")
    assert user["id"] == 1
    assert user["username"] == "alice"
    assert user["email"] == "alice@gmail.com"
    assert user["age"] == 15


def test_user_bob(get_user):
    user = get_user("user2")
    assert user["id"] == 2
    assert user["username"] == "bob"
    assert user["email"] == "bob@example.com"
    assert user["age"] == 25


def test_multiple_users(get_user):
    alice = get_user("user1")
    bob = get_user("user2")
    assert alice["age"] < bob["age"]
    assert alice["email"].endswith("gmail.com")
    assert bob["email"].endswith("example.com")


@pytest.fixture
def modify_alice_age(mock_user_data):
    original_age = mock_user_data["user1"]["age"]
    mock_user_data["user1"]["age"] = 18
    yield
    mock_user_data["user1"]["age"] = original_age


def test_modified_alice_age(get_user, modify_alice_age):
    alice = get_user("user1")
    assert alice["age"] == 18


@pytest.mark.parametrize(
    "user_key, expected_email",
    [("user1", "alice@gmail.com"), ("user2", "bob@example.com")],
)
def test_emails(get_user, user_key, expected_email):
    user = get_user(user_key)
    assert user["email"] == expected_email


@pytest.mark.xfail(reason="Work in progress")
def test_failing_case():
    assert 1 == 2


def test_dynamic_user(mock_user_data):
    mock_user_data["user3"] = {
        "id": 3,
        "username": "charlie",
        "email": "charlie@example.com",
        "age": 40,
    }
    assert mock_user_data["user3"]["age"] == 40
    del mock_user_data["user3"]
