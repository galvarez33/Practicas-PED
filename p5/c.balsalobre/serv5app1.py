import socket, sys, time, os

def servidor():
	server_address = ("localhost", 6351)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.bind(server_address)

	while True:
		print("Escuchando...")
		try:
			server_address, direccli = sock.recvfrom(64)
			if os.path.exists(server_address):

				ficherocompleto = open(server_address, "r", encoding = 'utf8')
				conexioncontenido = ficherocompleto.read(1024)

				while conexioncontenido != '':
					sock.sendto(conexioncontenido.encode('utf8'), direccli)
					ack = sock.recvfrom(1024)
					conexioncontenido = ficherocompleto.read(1024)
			
				ficherocompleto.close()
				sock.sendto("".encode('utf8'), direccli)
			
			else:
				sock.sendto("El fichero no existe o no hay permisos para abrirlo\n".encode('utf8'), direccli)
				sock.sendto("".encode('utf8'), direccli)
		
		except IOError as e:
			if e.errno == errno.EPIPE:
				pass



if __name__ == "__main__":
	
	try:
		servidor()
	except KeyboardInterrupt:
		print("\nCerrando Servidor...\n")

