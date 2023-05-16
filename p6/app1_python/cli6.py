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

    def ejecutar(self, path):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((self.direccion, self.puerto))

            try:
                if path == "cerrar":
                    sock.send(path.encode())
                    print(path)

                    # Esperar respuesta del servidor
                    respuesta = sock.recv(1024)
                    if respuesta.decode().strip() == "ok":
                        print(respuesta)
                        return

                else:
                    sock.send(path.encode())

                sock.settimeout(10)

                
                while True:
                    contenido = sock.recv(1024)
                    if not contenido:
                        break
                    os.write(1, contenido) 
                                  # con modulo os espera bytes, no str.Con file espera string
                                  
            except socket.timeout:
                print("Tiempo de espera agotado")
            finally:
                sock.shutdown(socket.SHUT_RDWR)

if __name__ == '__main__':
    direccion = 'localhost'
    puerto = 5000
    cliente = Cliente(direccion, puerto)
    cliente.ejecutar(f"{sys.argv[1]}\n")
