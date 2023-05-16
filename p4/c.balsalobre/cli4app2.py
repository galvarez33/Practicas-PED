import socket, sys, time, locale, errno
from datetime import datetime

# Idioma "es-ES" (código para el español de España)
locale.setlocale(locale.LC_ALL, 'es_ES.ISO8859-1')

server_address = '/tmp/p4cbalsalobre'

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM, 0)

sock.connect(server_address)

while True:
	fecha = sock.recv(64)
	if fecha:
		print("Fecha y hora: ", fecha.decode('utf8'))
		break

sock.close()
