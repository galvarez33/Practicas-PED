from user import User
import json

def test_user_has_username():
    verify_username_scenario("pepe")


def test_user_has_different_username():
    verify_username_scenario("juan")

def verify_username_scenario(username):
    user = User(username)
    assert user.name == username

def test_user_overloads_eq():
    user_1 = User("pepe")
    user_2 = User("pepe")

    assert user_1 == user_2

def test_user_overloads_hash():
    username = "pepe"
    user = User(username)

    assert hash(user) == hash(username)

def test_user_returns_username_hash_hash():
    username = "juan"
    user = User(username)

    assert hash(user) == hash(username)

def test_user_has_method_to_json():
    verify_to_json_scenario("pepe")

def test_user_has_method_to_json2():
    verify_to_json_scenario("juan")

def verify_to_json_scenario(username):
    user = User(username)

    expected_json = json.dumps({"name": username})
    assert user.to_json() == expected_json

def test_from_dict():
    username = "juan"
    user = User(username)
    user_dict = json.loads(user.to_json())
    read_user = User.from_dict(user_dict)
    assert read_user == user