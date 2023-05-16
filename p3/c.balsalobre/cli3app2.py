import os, sys, time, datetime, locale

# Idioma "es-ES" (código para el español de España)
locale.setlocale(locale.LC_ALL, 'es_ES.ISO8859-1')

def cliente():

	try:
		os.mkfifo(path)
	except FileExistsError:
		pass
	print("FIFO creado")
	
	lectura = open(path, 'r')
	datos = lectura.readline()
	print("Fecha y hora: ", datos)


if __name__ == '__main__':

	path = "fifo"

	cliente()