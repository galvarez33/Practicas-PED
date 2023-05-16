from user import User
from singleton import Singleton

class AuthManager(metaclass=Singleton):
    def __init__(self):
        self.logged_users = set()

    def validate(self, user):
        if user in self.logged_users:
            raise ValidationError
        else:
            self.logged_users.add(user)  

    def logout(self, user):
        self.logged_users.discard(user)

    
class ValidationError(Exception):
    pass
