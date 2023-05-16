import os
import socket
import setproctitle

# Cambiar el nombre del proceso
setproctitle.setproctitle("serv4")

# Verificar que el nombre haya sido cambiado
print(f"Nombre actual del proceso: {setproctitle.getproctitle()}")

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

sock.bind(('/tmp/prueba'))

print("Esperando conexiones")
sock.listen(1)

while True:
    con, h = sock.accept()
    print(f"\nSoy Proceso padre PID: {os.getpid()}")

    path = con.recv(4096)
    path = path.decode().strip()

    if path == "cerrar":
        print("El cliente cerró la conexión\nCerrando servidor...")
        con.send("ok".encode())
        con.close()
        sock.close()
        break

    else:
        print(f"Ruta recibida: {path}")

    pid = os.fork()

    if pid == 0:
        #proceso hijo maneja petición
        print(f"Proceso hijo PID {os.getpid()} envia el contenido \n\n")
        sock.close()  # Cerrar el socket para liberar descriptores, este solol debe manejar conn, no socket, de eso se encarga el padre. Pero como lo hereda hay que cerrarlo
        con.send("Conexión recibida".encode())

        fd = os.open(path, os.O_RDONLY)
        MAX_BYTES = 1024
        data = os.read(fd, MAX_BYTES)

        while data:
            con.send(data)
            data = os.read(fd, MAX_BYTES)

        con.close()
        os._exit(0)  # Salir del proceso hijo

    else:
        # Proceso padre
        con.close()
