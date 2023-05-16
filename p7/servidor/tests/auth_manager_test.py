from auth_manager import AuthManager
from auth_manager import ValidationError
from user import User
import pytest

@pytest.fixture(autouse=True)
def build_auth_manager_scenario():
    yield
    AuthManager().logged_users = set()

def test_auth_manager_has_logged_users_set():
    auth_manager = AuthManager()
    assert isinstance(auth_manager.logged_users, set)

def test_auth_manager_validate_adds_user_to_set():
    auth_manager = AuthManager()
    user = User("pepe") 

    auth_manager.validate(user)
    assert user in auth_manager.logged_users

def test_auth_manager_validate_throws_exception_when_adding_same_user_twice():
    auth_manager = AuthManager()
    user = User("pepe") 

    auth_manager.validate(user)
    with pytest.raises(ValidationError):
        auth_manager.validate(user)

def test_auth_manager_logout_user():
    auth_manager = AuthManager()
    user = User("pepe") 

    auth_manager.validate(user)
    auth_manager.logout(user)

    assert not user in auth_manager.logged_users

def test_auth_manager_is_singleton():
    am1 = AuthManager()
    am2 = AuthManager()
    assert am1 == am2