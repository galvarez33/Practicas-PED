import sys
import socket
import setproctitle
import os

# Cambiar el nombre del proceso
setproctitle.setproctitle("cli6")

class Cliente:
    
    def __init__(self, direccion, puerto):
        self.direccion = direccion
        self.puerto = puerto
        self.sock = None

    def ejecutar(self, path):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.direccion, self.puerto))

        self.sock.send(path.encode())s
        

        while True:
            contenido = self.sock.recv(1024)
            if not contenido:
                break
            os.write(1, contenido)

    def cierre(self):
        if self.sock:
            self.sock.close()

if __name__ == '__main__':
    direccion = 'localhost'
    puerto = 5000
    cliente = Cliente(direccion, puerto)
    try:
        cliente.ejecutar(f"{sys.argv[1]}\n")
    finally:
        cliente.cierre()
