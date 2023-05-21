import os
import socket
import select
import sys

direccion = 'localhost'
puerto = 5001

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind((direccion, puerto))
print("Esperando conexiones...")
sock.listen(1)

conexiones = []  # Lista para almacenar las conexiones
usuarios = []

while True:
    lectura, _, _ = select.select([sock] + conexiones, [], [])

    for socket_listo in lectura:
        if socket_listo == sock:
    # Nueva conexión entrante
            con, _ = sock.accept()
            conexiones.append(con)
            nuevo_usuario = con.recv(1024)  # Recibir datos en el nuevo socket de conexión
            nuevo_usuario = nuevo_usuario.decode()  # Decodificar los datos recibidos
            if nuevo_usuario not in usuarios:
                usuarios.append(nuevo_usuario)
                con.send("usuario registrado".encode())  # Enviar la respuesta como bytes
            else:
                con.send("NACK".encode())  # Enviar la respuesta como bytes



        else:
            # Mensaje recibido de un cliente existente
            mensaje = socket_listo.recv(1024)
            mensaje = mensaje.decode().strip()

            if not mensaje:
                # Cliente desconectado
                print("Cliente desconectado")
                socket_listo.close()
                conexiones.remove(socket_listo)
                continue

            print(f"Mensaje recibido: {mensaje}")

            if mensaje.lower() == "cerrar":
                # Cliente solicita cerrar la conexión
                print("Cliente solicitó cerrar la conexión")
                socket_listo.close()
                conexiones.remove(socket_listo)

                # Terminar el proceso hijo
                pid = os.fork()
                if pid == 0:
                    sock.close()
                    for cliente in conexiones:
                        cliente.close()
                    os._exit(0)
            
            for cliente in conexiones:
                if cliente != socket_listo:  # No reenviar el mensaje al cliente actual
                    try:
                        cliente.send(mensaje.encode())
                    except socket.error as e:
                        print(f"Error al enviar mensaje al cliente: {e}")
