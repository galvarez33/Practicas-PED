import sys
import socket
import setproctitle
import os 
# Cambiar el nombre del proceso
setproctitle.setproctitle("cli4")



class Cliente:
    
    def __init__(self,nombre_socket):
        self.nombre_socket= nombre_socket

        
    def ejecutar(self,path):

        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        sock.connect((self.nombre_socket))
        
        try:
            if path == "cerrar":
                sock.send(path.encode())
                print(path)

                # Esperar respuesta del servidor
                respuesta = sock.recv(4096)
                if respuesta.decode().strip() == "ok":
                    print(respuesta)
                    return

            else:
                sock.send(path.encode())


            while True:
                    contenido = sock.recv(1024)
                    if not contenido:
                        break
                    os.write(1, contenido) 

        finally:
            sock.shutdown(socket.SHUT_RDWR)
            sock.close()

if __name__ == '__main__':
    nombre_socket = '/tmp/prueba'
    cliente = Cliente(nombre_socket)
    cliente.ejecutar(f"{sys.argv[1]}\n")
