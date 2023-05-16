from user import User
from message import Message
import json
import os

class Chat:
    def from_dict(chat_dict):
        id = chat_dict["id"]
        
        users = [json.loads(user_str) for user_str in chat_dict["users"]]
        users = [User.from_dict(user_dict) for user_dict in users]

        messages = [json.loads(message_str) for message_str in chat_dict["messages"]]
        messages = [Message.from_dict(message_dict) for message_dict in messages]
        
        return Chat(id, users, messages)

    def __init__(self, id, users, messages=[]):
        self.users = users
        self.messages = messages
        self.id = id

    def __eq__(self, other):
        return self.to_json() == other.to_json()

    def to_json(self):
        return json.dumps(
            {   
                "id": self.id,
                "users": [user.to_json() for user in self.users], 
                "messages": [message.to_json() for message in self.messages]
            })
    
    def add_message(self, message):
        self.messages.append(message)
        FileManager.save(self)
        
class FileManager:
    def save(chat):
        dir = os.path.dirname(__file__)
        file = open(os.path.join(dir, "..", "chats", chat.id), "w")
        file.write(chat.to_json())
        file.close()

    def load_chats():
        chats = []

        current_dir = os.path.dirname(__file__)
        chats_path = os.path.join(current_dir, "..", "chats")
        for filename in os.listdir(chats_path):
            path = os.path.join(chats_path, filename)
            chat = FileManager.__load_chat(path)
            chats.append(chat)

        return chats
    
    def __load_chat(path):
        file = open(path, "r")
        chat_dict = json.loads(file.read())
        return Chat.from_dict(chat_dict)

