import os, sys, time, locale
from datetime import datetime

locale.setlocale(locale.LC_ALL, '')

rd1, wd1 = os.pipe()

r1, w1 = os.fdopen(rd1, 'rb', 0), os.fdopen(wd1, 'wb', 0)

pid = os.fork()

if pid:
	r1.close() #Se cierra lecutra en pipe
	mensaje = str(datetime.now(). strftime("%A, %d de %B de %Y, %X %Z"))
	w1.write(mensaje.encode('utf8'))

else:
	w1.close() #Se cierra escritura en pipe
	datos = r1.read()
	print("Fecha y hora: " + datos.decode('utf8').strip())