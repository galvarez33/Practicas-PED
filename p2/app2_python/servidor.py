import os
import time

class Servidor:
    def __init__(self, read_pipe, write_pipe):
        self.read_pipe = read_pipe
        self.write_pipe = write_pipe
        
    def run(self):
        while True:
            mensaje = self.read_pipe.read().decode().rstrip()
            if mensaje == "Solicitud de hora":
                print('Solicitud de hora recibida en %s' % time.asctime())
                respuesta = time.strftime('%H:%M:%S') + '\n'
                self.write_pipe.write(respuesta.encode())
                self.write_pipe.flush()
