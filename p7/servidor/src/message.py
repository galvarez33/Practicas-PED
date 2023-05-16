from user import User
import json

class Message:

    def from_dict(message_dict):
        user_dict = json.loads(message_dict["sender"])
        sender = User.from_dict(user_dict)
        content = message_dict["content"]
        chat_id = message_dict["chat_id"]
        return Message(sender, content, chat_id)

    def __init__(self, sender, content, chat_id):
        self.sender = sender
        self.content = content
        self.chat_id = chat_id

    def to_json(self):
        return  json.dumps(
            {   
                "chat_id": self.chat_id,
                "sender": self.sender.to_json(), 
                "content": self.content
            })

    def __eq__(self, other):
        return self.sender == other.sender and self.content == other.content and self.chat_id == other.chat_id