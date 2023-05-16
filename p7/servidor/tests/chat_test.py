from user import User
from message import Message
from chat import Chat
import json
import os

def test_chat_has_users_set():
    chat = Chat("id", set())
    assert isinstance(chat.users, set)

def test_chat_stores_user_set():
    users = set()
    chat = Chat("id", users)
    assert users is chat.users

def test_chat_stores_messages_list():
    messages = []
    chat = Chat("id", set(), messages)
    assert messages is chat.messages

def test_chat_has_to_json_method():
    users = {User("pepe"), User("juan")}
    messages = [Message(User("pepe"), "hola", "1"), Message(User("juan"), "adios","2") ]
    chat = Chat("id", users, messages)

    expected_json = json.dumps(
        {   
            "id": chat.id,
            "users": [user.to_json() for user in chat.users], 
            "messages": [message.to_json() for message in chat.messages]
        })
    
    
    assert expected_json == chat.to_json()
    
def test_add_message_adds_message_to_list():
    users = {User("pepe"), User("juan")}
    chat = Chat("id", users)

    msg = Message(User("pepe"), "Holaaaa", "1")
    chat.add_message(msg)

    assert msg in chat.messages

def test_chat_has_identifier():
    id = "id"
    chat = Chat(id, set(), [])
    assert chat.id == id

def test_chat_stores_real_identifier():
    id = "different id"
    chat = Chat(id, set(), [])
    assert chat.id == id

def test_chat_eq():
    chat1 = Chat("id", set(), [])
    chat2 = Chat("id", set(), [])
    assert chat1 == chat2

def test_chat_from_dict():
    id = "1"
    chat = Chat(id, set(), [])
    chat_dict = json.loads(chat.to_json())

    read_chat = Chat.from_dict(chat_dict) 
    print(chat.to_json())
    assert read_chat == chat

def test_add_message_dumps_chat_to_file():
    users = {User("pepe"), User("juan")}
    chat = Chat("id", users)

    msg = Message(User("pepe"), "Holaaaa", "1")
    chat.add_message(msg)
    
    dir = os.path.dirname(__file__)
    path = os.path.join(dir, "..", "chats", chat.id)
    saved_json = open(path, "r").read()

    assert chat.to_json() == saved_json

    if os.path.exists(path):
        os.remove(path)
