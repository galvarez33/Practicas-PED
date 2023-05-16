import os
import time


class Servidor:
    def __init__(self, nombre_fifo):
        self.nombre_fifo = nombre_fifo
        
    def ejecutar(self):
        if not os.path.exists(self.nombre_fifo):
            os.mkfifo(self.nombre_fifo)
        print("\nEsperando petición del cliente")
                                                       
        while True:
            with open(self.nombre_fifo, 'r') as fifo_lectura:
                    entrada = fifo_lectura.readline()

                    if entrada.lower() == "hora":
                        print('Solicitud de hora recibida en %s' % time.asctime())
                        mensaje = time.strftime('%H:%M:%S') + '\n'
                        with open(self.nombre_fifo, 'w') as fifo_escritura:
                            fifo_escritura.write(mensaje)
                    
                    elif entrada.lower()== "cerrar":
                        with open(self.nombre_fifo, 'w') as fifo_escritura:
                            fifo_escritura.write(entrada)
                            print("\nCliente cierra conexion, saliendo...\n")
                            break

                    else:
                        with open(self.nombre_fifo, 'w') as fifo_escritura:
                            fifo_escritura.write("Entrada no válida")
                        


if __name__ == '__main__':
    nombre_fifo = 'prueba_fifo'
    servidor = Servidor(nombre_fifo)
    servidor.ejecutar()
