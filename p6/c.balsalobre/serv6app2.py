import socket, sys, time, os, locale, errno
from datetime import datetime

# Idioma "es-ES" (código para el español de España)
locale.setlocale(locale.LC_ALL, 'es_ES.ISO8859-1')

def servidor():
	server_address = ("localhost", 3003)

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
	sock.bind(server_address)
	sock.listen()

	while True:
	
		print("Esperando conexión")
		conexion, client_address = sock.accept()

		try:
			while True:
				fecha = str(datetime.now().strftime("%A, %d de %B de %Y, %X %Z \n"))
				conexion.send(fecha.encode('utf8'))
				conexion.close()

		except IOError as er:
			if er.errno == errno.EPIPE:
				pass


if __name__ == "__main__":

	try:
		servidor()
	except KeyboardInterrupt:
		print("\nCerrando Servidor...\n")