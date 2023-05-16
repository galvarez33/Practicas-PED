import os
import sys


class Cliente:
    def __init__(self, nombre_fifo):
        self.nombre_fifo = nombre_fifo
        
    def ejecutar(self,entrada):
        with open(self.nombre_fifo, 'w') as fifo_escritura:
            fifo_escritura.write(entrada)

        while True:  
            with open(self.nombre_fifo, 'r') as fifo_lectura:
                respuesta = fifo_lectura.readline()
                
                if respuesta.lower() == "cerrar":
                    print("saliendo")

                elif entrada.lower() == "hora": 
                    print("La hora actual es:", respuesta)

                    
                else:
                    print(respuesta)
                    
            break

if __name__ == '__main__':
    nombre_fifo = 'prueba_fifo'
    cliente = Cliente(nombre_fifo)
    while True:
        entrada = input ("\nDesea recibir HORA o CERRAR : ")
        cliente.ejecutar(entrada)
        break
    
    
