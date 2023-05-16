from user import User
from socket_manager import SocketManager
import socket
import pytest

@pytest.fixture(autouse=True)
def build_auth_manager_scenario():
    yield
    try:
        SocketManager().user_socket_map.clear()
        del SocketManager().server_socket
    except AttributeError:
        pass

def test_socket_manager_is_singleton():
    sm1 = SocketManager()
    sm2 = SocketManager()
    assert sm1 == sm2

def test_stores_server_socket():
    server_socket = socket.socket()
    socket_manager = SocketManager()
    socket_manager.initialize(server_socket)
    assert socket_manager.server_socket == server_socket

def test_register_map_user_to_socket():
    user = User("juan")
    s =  socket.socket()
    socket_manager = SocketManager()
    socket_manager.register(user, s)

    assert socket_manager.user_socket_map[user] == s


def test_register_map_socket_to_user():
    user = User("juan")
    s =  socket.socket()
    socket_manager = SocketManager()
    socket_manager.register(user, s)

    assert socket_manager.socket_user_map[s] == user

def test_remove_register_map_user_to_socket():
    user = User("juan")
    s =  socket.socket()
    socket_manager = SocketManager()
    socket_manager.register(user, s)

    socket_manager.remove(user)

    assert user not in socket_manager.user_socket_map.keys() 

def test_remove_register_map_socket_to_user():
    user = User("juan")
    s =  socket.socket()
    socket_manager = SocketManager()
    socket_manager.register(user, s)

    socket_manager.remove(user)

    assert s not in socket_manager.socket_user_map.keys() 