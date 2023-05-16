from auth_manager import AuthManager, ValidationError
from socket_manager import SocketManager

class Command:
    def run(self):
        raise NotImplementedError()

class LoginCommand(Command):
    def __init__(self, user, socket):
        self.user = user
        self.socket = socket

    def run(self):
        try:
            AuthManager().validate(self.user)
            SocketManager().register(self.user, self.socket)
            self.socket.send(f"Bienvenido {self.user.name}".encode("utf8"))
        except ValidationError:
            self.socket.send(f"No se pudo iniciar sesión como '{self.user.name}'".encode("utf8"))

class LogoutCommand(Command):
    def __init__(self, user):
        self.user = user
    
    def run(self):
        AuthManager().logout(self.user)
        socket_manager = SocketManager()
        socket_manager.send_string(self.user, f"Adiós, '{self.user.name}'".encode("utf8"))
        socket_manager.remove(self.user)
