import os
import sys
import binascii
import io



class Cliente:
    def __init__(self, ida_fifo,vuelta_fifo):
        self.ida_fifo = ida_fifo
        self.vuelta_fifo = vuelta_fifo
        
    def ejecutar(self,path):
        with open(self.ida_fifo, 'wb') as fifo_escritura:
            path = path.encode("utf8")
            fifo_escritura.write(path)
            fifo_escritura.flush()
            fifo_escritura.close()

    
        
        with open(self.vuelta_fifo, 'rb') as fifo_lectura:
            
            while True: 
                line = fifo_lectura.readline()
                if not line:
                    break
                os.write(1, line)               
        fifo_lectura.close()

if __name__ == '__main__':
    ida_fifo = 'ida_fifo'
    vuelta_fifo = 'vuelta_fifo'
    cliente = Cliente(ida_fifo,vuelta_fifo)
    cliente.ejecutar(f"{sys.argv[1]}\n")
