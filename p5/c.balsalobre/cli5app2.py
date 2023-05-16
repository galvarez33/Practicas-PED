import socket, sys, time, locale, errno
from datetime import datetime

# Idioma "es-ES" (código para el español de España)
locale.setlocale(locale.LC_ALL, 'es_ES.ISO8859-1')

direc = ("0.0.0.0", 0) #del cliente
server_address = ("localhost", 7000)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
sock.bind(direc)

while True:
	sock.sendto("direccli".encode('utf8'), server_address)
	fecha = sock.recvfrom(64)
	print("Fecha y hora: ", fecha[0].decode('utf8'))
