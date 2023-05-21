import sys
import socket
import os
import select

class Cliente:
    
    def __init__(self, direccion, puerto):
        self.direccion = direccion
        self.puerto = puerto
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.direccion, self.puerto))
        self.sock.settimeout(10)

    def recibir_mensajes(self, usuario):
        while True:
            ready, _, _ = select.select([self.sock, sys.stdin], [], [])
            for socket_listo in ready:
                if socket_listo == self.sock:
                    contenido = self.sock.recv(1024)
                    if not contenido:
                        break
                    mensaje_recibido = contenido.decode()
                    print(f"{mensaje_recibido}\n")  # Imprimir el mensaje recibido con el usuario que lo envió
                elif socket_listo == sys.stdin:
                    mensaje = sys.stdin.readline().strip()
                    if mensaje == "cerrar":
                        return
                    self.sock.send(mensaje.encode())

    def ejecutar(self):
        usuario = input("Nombre de usuario:")

        # Iniciar el hilo para recibir mensajes
        import threading
        threading.Thread(target=self.recibir_mensajes, args=(usuario,), daemon=True).start()

        # Mostrar el nombre de usuario antes del bucle de envío de mensajes
        print(f"{usuario}: ")

        while True:
            mensaje = input()
            mensaje = f"{usuario}: {mensaje}"  # Agregar el usuario al mensaje
            self.sock.send(mensaje.encode())
            if mensaje == "cerrar":
                break

        self.sock.shutdown(socket.SHUT_RDWR)
        self.sock.close()

if __name__ == '__main__':
    direccion = 'localhost'
    puerto = 5000
    cliente = Cliente(direccion, puerto)
    cliente.ejecutar()
