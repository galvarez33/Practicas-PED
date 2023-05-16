import os, sys, time, locale
from datetime import datetime

# Idioma "es-ES" (código para el español de España)
locale.setlocale(locale.LC_ALL, 'es_ES.ISO8859-1')

def server():
    
    try:
        os.mkfifo(sc)
    except FileExistsError:
        pass
    print("FIFO creado")

    escritura = open(sc, 'w')
    fechahora = str(datetime.now().strftime("%A, %d de %B de %Y, %X %Z"))
    escritura.write(fechahora)

if __name__ == '__main__':
    sc = "fifo"
    
    if not os.path.exists(sc):
        os.mkfifo(sc)

    try:
        server()
    except KeyboardInterrupt:
        print("\nCerrando Servidor...\n")
