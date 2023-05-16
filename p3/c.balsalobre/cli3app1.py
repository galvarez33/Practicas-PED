import os, sys
from time import sleep

fifo = "fifo"
mensaje = input("Fichero: ") + " \n"

def cliente():

	fifowrite = open(fifo, "w")
	pid = str(os.getpid())
	request = pid + " " + mensaje
	fifowrite.write(request)
	fifowrite.close()

	fiforeadmensaje = fifo + "_{}".format(pid)
	try:
		os.mkfifo(fifo + "_{}".format(pid))
	except FileExistsError:
		pass

	fiforead = open(fiforeadmensaje, "rb")
	text = fiforead.read()
	fiforead.close()
	os.write(1, text)
	os.unlink(fiforeadmensaje)

if __name__ == "__main__":
	try:
		os.mkfifo(fifo)
	except FileExistsError:
		pass
	cliente()