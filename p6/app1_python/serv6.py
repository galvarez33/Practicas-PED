import os
import socket
import setproctitle

#Cambiar el nombre del proceso
setproctitle.setproctitle("serv6")

# Verificar que el nombre haya sido cambiado
print(f"\nNombre actual del proceso: {setproctitle.getproctitle()}")

direccion = 'localhost'
puerto = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind((direccion, puerto)) 

print ("Esperando conexiones...")
sock.listen(1)

while True:
    con, h = sock.accept()
    print(f"\nSoy Proceso padre PID: {os.getpid()}")

    path = con.recv(1024)
    path = path.decode().strip()

    if path == "cerrar":
        print("El cliente cerró la conexión\nCerrando servidor...")
        con.send(b"ok")
        con.close()
        sock.close()
        break

    else:
        print(f"Ruta recibida: {path}")

    pid = os.fork()

    if pid == 0:
        # Proceso hijo
        print(f"Proceso hijo PID {os.getpid()} envia el contenido \n\n")
        sock.close()  # Cerrar el socket en el proceso hijo

        try:
            with open(path, 'rb') as file:
                while True:
                    data = file.read(1024)
                    if not data:
                        break
                    con.send(data)
        except FileNotFoundError:
            con.send(b"El archivo no existe")

        con.shutdown(socket.SHUT_RDWR)
        con.close()
        os._exit(0)

    else:
        # Proceso padre
        con.close()