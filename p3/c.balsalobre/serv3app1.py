import os, sys
from time import sleep

fifo = "fifo"

def servidor():

	fiforead = open(fifo, 'r')
	while True:
		mensajecliente = fiforead.readline().split()
		if len(mensajecliente) == 0:
			continue
		elif len(mensajecliente) > 2:
			print("Error en el input.")
			continue

		pidcliente = str(mensajecliente[0])
		try:
			fichero = open(mensajecliente[1], 'rb')
			texto = fichero.read()
			fichero.close()

			fifowrite = open(fifo + "_{}".format(pidcliente), 'wb')
			fifowrite.write(texto)
			fifowrite.close()

			sleep(5)

		except FileNotFoundError:
			fifowrite = open(fifo + "_{}".format(pidcliente), 'w')
			fifowrite.write("error al abrir el fichero")
			fifowrite.close()

if __name__ == "__main__":
	try:
		os.mkfifo(fifo)
	except FileExistsError:
		pass

	try:
		servidor()
	except KeyboardInterrupt:
		print("\nCerrando Servidor...\n")
