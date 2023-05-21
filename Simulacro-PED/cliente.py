import socket

class Cliente:
    def __init__(self, direccion):
        self.direccion = direccion

    def enviar_solicitud(self, solicitud):
        cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente_socket.connect(self.direccion)

        cliente_socket.sendall(solicitud.encode('utf-8'))

        respuesta = cliente_socket.recv(1024).decode('utf-8')

        print('Respuesta del servidor:', respuesta)

        cliente_socket.close()

direccion_servidor = ('localhost', 8080)
cliente = Cliente(direccion_servidor)

for _ in range(3):
    solicitud = input('Ingrese "hora" o "fecha": ')
    cliente.enviar_solicitud(solicitud)
