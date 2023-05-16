from socket_manager import SocketManager
from user import User
from chat import Chat
from message import Message
from commands import Command, LoginCommand, LogoutCommand, SendMessageCommand
from unittest import mock
from auth_manager import AuthManager
import socket
import pytest

@pytest.fixture(autouse=True)
def set_up():
    SocketManager().user_socket_map.clear()
    SocketManager().socket_user_map.clear()
    AuthManager().logged_users = set()
    yield

def test_command_has_run_method():
    cmd = Command()
    with pytest.raises(NotImplementedError):
        cmd.run()

def test_login_command_is_command():
    cmd = LoginCommand(User("pepe"), socket.socket())
    assert isinstance(cmd, Command)

def test_login_command_stores_user():
    user = User("pepe")
    cmd = LoginCommand(user, socket.socket())
    assert cmd.user == user

def test_login_command_stores_socket():
    user = User("pepe")
    s = socket.socket()
    cmd = LoginCommand(user, s)
    assert cmd.socket == s

def test_login_command_sends_ok_message_if_login_successful():
    # Setup test and mock socket
    user = User("pepe")
    s = mock.Mock()
    cmd = LoginCommand(user, s)

    # Run command twice
    cmd.run()

    # Expect socket to have been called with correct message
    s.send.assert_called_once_with(f"Bienvenido {user.name}".encode("utf8")) 

def test_login_command_sends_error_message_if_user_has_already_logged_in():
    # Setup test and mock socket
    user = User("pepe")
    s = mock.Mock()
    cmd = LoginCommand(user, s)

    # Run command twice
    cmd.run()
    cmd.run()

    # Expect socket to have received error message
    s.send.assert_called_with(f"No se pudo iniciar sesión como '{user.name}'".encode("utf8")) 

def test_login_command_registers_user():
    # Setup test and mock socket
    user = User("pepe")
    s = mock.Mock()
    cmd = LoginCommand(user, s)

    # Run command
    cmd.run()

    # Expect user to be register
    assert SocketManager().user_socket_map[user] is s

def test_logout_command_is_command():
    user = User("pepe")
    cmd = LogoutCommand(user)
    assert isinstance(cmd, Command)

def test_logout_command_stores_socket():
    user = User("pepe")
    cmd = LogoutCommand(user)
    assert cmd.user == user

def test_send_message_command_stores_chat():
    chat = Chat("1", set(), [])
    message =  Message("juan", "hola", "2")
    cmd = SendMessageCommand(chat, message)
    assert cmd.chat == chat 

def test_send_message_command_stores_message():
    chat = Chat("1", set(), [])
    message =  Message("juan", "hola", "2")
    cmd = SendMessageCommand(chat, message)
    assert cmd.message == message
