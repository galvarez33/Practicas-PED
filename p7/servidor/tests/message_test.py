
from chat import Chat
from message import Message
from user import User
import json

def test_message_has_chat_id():
    message_has_chat_scenario("chat1")

def test_message_has_chat_id2():
    message_has_chat_scenario("chat2")

def message_has_chat_scenario(chat_id):
    chat_id = "1"
    message = Message(User("pepe"), "hola", chat_id)
    assert message.chat_id == chat_id



def test_message_has_sender():
    message_has_sender_scenario("pepe")

def test_message_has_sender2():
    message_has_sender_scenario("juan")

def message_has_sender_scenario(username):
    sender = User(username)
    message = Message(sender, "hola", "1")
    assert message.sender == sender 

def test_message_has_content():
    verify_message_has_content_scenario("hola")

def test_message_has_content2():
    verify_message_has_content_scenario("adios")

def verify_message_has_content_scenario(content):
    message = Message(User("pepe"), content, "1")
    assert message.content == content

def test_message_to_json():
    sender = User("pepe")
    content = "hola"
    chat_id = "1"
    verify_message_to_json_scenario(sender, content, chat_id)

def test_message_to_json2():
    sender = User("juan")
    content = "adios"
    chat_id = "1"
    verify_message_to_json_scenario(sender, content, chat_id)

def verify_message_to_json_scenario(sender, content, chat_id):
    message = Message(sender, content, chat_id)

    expected_json = json.dumps(
        {  
            "chat_id":chat_id, 
            "sender": sender.to_json(), 
            "content": content
        })
    
    assert expected_json == message.to_json()

def test_message_implements_eq():
    message_1 = Message(User("pepe"), "hola", "1")
    message_2 = Message(User("pepe"), "hola", "1")
    assert message_1 == message_2

def test_message_implements_eq_with_all_data():
    message_1 = Message(User("pepe"), "hola", "1")
    message_2 = Message(User("pepe"), "adios", "2")
    assert message_1 != message_2

def test_from_dict():
    message = Message(User("juan"), "hola", "1")
    message_dict = json.loads(message.to_json())

    read_message = Message.from_dict(message_dict)
    assert read_message == message
