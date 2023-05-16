import socket, sys, time, os

def servidor():

	while True:
		
		if os.path.exists(server_address):
			os.unlink(server_address)

		sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

		sock.bind(server_address)

		print("Comenzando en {}".format(server_address))

		sock.listen(10)
		print("Socket escuchando")

		print("Esperando conexión")
		conexion, client_address = sock.accept()

		try:
			fichero = conexion.recv(64)
			ficherocompleto = open(fichero, "r")
			conexioncontenido = ficherocompleto.read(1024)

			while conexioncontenido != '':
				conexion.send(conexioncontenido.encode('utf8'))
				conexioncontenido = ficherocompleto.read(1024)

		except FileNotFoundError:
			conexion.sendall("Error al abrir el fichero\n".encode('utf8'))

		ficherocompleto.close()
		conexion.close()


if __name__ == "__main__":

	server_address = '/tmp/s_p4_balsalobre'
		
	try:
		servidor()
	except KeyboardInterrupt:
		print("\nCerrando Servidor...\n")
	

