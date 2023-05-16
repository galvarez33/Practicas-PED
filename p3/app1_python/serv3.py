import os
import time


class Servidor:
    def __init__(self, ida_fifo, vuelta_fifo):
        self.ida_fifo = ida_fifo
        self.vuelta_fifo = vuelta_fifo
        
    def ejecutar(self):
        if not os.path.exists(self.ida_fifo):
            os.mkfifo(self.ida_fifo) 
        if not os.path.exists(self.vuelta_fifo):
            os.mkfifo(self.vuelta_fifo) 
        print("\nEsperando petición del cliente")
           
        while True:
            with open(self.ida_fifo, 'rb') as fifo_lectura:

                    path = fifo_lectura.read()
                    path = path.decode('utf-8').strip()               
                    
                    print(f"El servidor recibe: {path}")
                         

            with open(self.vuelta_fifo, 'wb') as fifo_escritura: 
                l = []
                
                try:
                    with open(path,"rb") as file:
                        for line in file:
                            l.append(line)
                            
                            fifo_escritura.write(line)
                            fifo_escritura.flush()                                                            
                        fifo_escritura.close()
                
                except Exception as e:
                    
                    fifo_escritura.write(f"Error al intentar abrir el fichero: {path}".encode("utf-8"))
                            


if __name__ == '__main__':
    ida_fifo = 'ida_fifo'
    vuelta_fifo= 'vuelta_fifo'
    servidor = Servidor(ida_fifo,vuelta_fifo)
    servidor.ejecutar()
