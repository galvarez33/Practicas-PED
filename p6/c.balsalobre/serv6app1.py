import socket, sys, time, os, errno

def servidor():
	server_address = ("localhost", 3001)
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind(server_address)
	sock.listen(10)

	while True:
		conexion, client_address = sock.accept()
		print("Escuchando...")
		try:
			fichero = conexion.recv(64)
			if os.path.exists(fichero):
				try:
					ficherocompleto = open(fichero, "r")
					conexioncontenido = ficherocompleto.read(1024)

					while conexioncontenido != '':
						conexion.send(conexioncontenido.encode('utf8'))
						conexioncontenido = ficherocompleto.read(1024)
					ficherocompleto.close()

				except FileNotFoundError:
					conexion.sendall("Error al abrir el fichero\n".encode('utf8'))
		
			conexion.close()

		except IOError as e:
			if e.errno == errno.EPIPE:
				pass

if __name__ == "__main__":

	try:
		servidor()
	except KeyboardInterrupt:
		print("\nCerrando Servidor...\n")

