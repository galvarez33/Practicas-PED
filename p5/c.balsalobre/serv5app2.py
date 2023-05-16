import socket, sys, time, os, locale
from datetime import datetime

# Idioma "es-ES" (código para el español de España)
locale.setlocale(locale.LC_ALL, 'es_ES.ISO8859-1')

def servidor():
	server_address = ("localhost", 7000)

	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
	sock.bind(server_address)

	while True:
		print("Esperando conexión")
		try:
			datos, direccli = sock.recvfrom(64)
			fecha = str(datetime.now().strftime("%A, %d de %B de %Y, %X %Z \n"))
			sock.sendto(fecha.encode('utf8'), direccli)

		except IOError as er:
			if er.errno == errno.EPIPE:
				pass

if __name__ == "__main__":
	
	try:
		servidor()
	except KeyboardInterrupt:
		print("\nCerrando Servidor...\n")
