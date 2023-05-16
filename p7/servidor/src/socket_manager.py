from singleton import Singleton
import socket
import select

class SocketManager(metaclass=Singleton):
    def __init__(self):
        self.user_socket_map = {}
        self.socket_user_map = {}
        self.server_socket = None

    def initialize(self, server_socket):
        self.server_socket = server_socket

    def register(self, user, socket):
        self.user_socket_map[user] = socket
        self.socket_user_map[socket] = user

    def remove(self, user):
        s = self.user_socket_map[user]
        del self.user_socket_map[user] 
        del self.socket_user_map[s] 

    def wait_for_connections(self):
        r_list = [self.server_socket] + self.user_socket_map.values()
        ready_sockets, _, _ = select.select(r_list, [], [])
        return ready_sockets

    def send_string(self, user, string):
        socket = self.user_socket_map[user]
        socket.send(string.encode("utf8"))

    def send_message(self, user, message):
        socket = self.user_socket_map[user]
        socket.send(message.to_json().encode("utf8"))
        