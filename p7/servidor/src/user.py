import json

class User:
    def __init__(self, username):
        self.name = username
    
    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)
    
    def to_json(self):
        return json.dumps({"name": self.name})
    
    def from_dict(user_dict):
        name = user_dict["name"]
        return User(name)
