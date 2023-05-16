import os , sys

rd1, wd1 = os.pipe()
rd2, wd2 = os.pipe()

r1, w1 = os.fdopen(rd1, 'rb', 0), os.fdopen(wd1, 'wb', 0)
r2, w2 = os.fdopen(rd2, 'rb', 0), os.fdopen(wd2, 'wb', 0)

pid = os.fork()

if pid:
	w1.close() #Se cierra escritura en el pipe 1
	datos = r1.readline()
	r2.close() #Se cierra lectura en el pipe 2

	try:
		file = open(datos.decode('utf8').strip(), 'r')
		text = file.read()
		file.close()

	except FileNotFoundError as er:
		print("Error de fichero: ", er)
	
	w2.write(text.encode('utf8'))

else:
	r1.close() #Se cierra lectura en el pipe 1
	message = input("Fichero: ") + " \n"

	w1.write(message.encode('utf8'))
	w2.close() #Se cierra escritura en el pipe 2
	datos2 = r2.read()
	print("Lectura del fichero: %s \n" % (datos2.decode('utf8').strip()))
