import time
import os
from cliente import Cliente


class Manager:
    def gestionar_solicitud(self, solicitud):
        if solicitud == "cerrar":
            cliente = Cliente("localhost", 8080)
            cliente.cierre()
            respuesta = "Cliente cerrado\n"
            return respuesta.encode()
        
        l = []
        try:
            with open(solicitud, 'rb') as file:
                while True:
                    data = file.read(1024)
                    if not data:
                        break
                    l.append(data)
        except:
            respuesta = "Fichero no encontrado"
            return respuesta.encode()
        
        return b''.join(l)



           
