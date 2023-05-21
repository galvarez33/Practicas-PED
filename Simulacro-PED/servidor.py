import socket
from manager import Manager

class Servidor:
    def __init__(self, direccion):
        self.direccion = direccion

    def iniciar(self):
        servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        servidor_socket.bind(self.direccion)
        servidor_socket.listen(1)
        print('Servidor iniciado en', self.direccion)

        while True:
            conexion_cliente, direccion_cliente = servidor_socket.accept()
            print('Conectado a:', direccion_cliente)

            # Recibir solicitud del cliente
            solicitud = conexion_cliente.recv(1024).decode('utf-8')

            # Enviar la solicitud al Manager
            respuesta = Manager().gestionar_solicitud(solicitud)
            print(f"mandando : {respuesta}")
            # Enviar respuesta al cliente
            conexion_cliente.sendall(respuesta.encode('utf-8'))

            conexion_cliente.close()

if __name__ == '__main__':
    # Definir la dirección del servidor
    direccion_servidor = ('localhost', 8080)

    # Crear una instancia del servidor
    servidor = Servidor(direccion_servidor)

    # Iniciar el servidor
    servidor.iniciar()




























    
  