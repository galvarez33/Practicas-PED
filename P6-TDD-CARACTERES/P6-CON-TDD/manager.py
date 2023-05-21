import time
import os
from cliente import Cliente


class Manager:
    def contar_lineas(self, fichero):
        with open(fichero, 'r') as file:
            lineas = file.readlines()
        return len(lineas)

    def contar_caracteres(self, fichero):
        with open(fichero, 'r') as file:
            contenido = file.read()
        return len(contenido)

    def contar_palabras(self, fichero):
        with open(fichero, 'r') as file:
            contenido = file.read()
        palabras = contenido.split()
        return len(palabras)

    def gestionar_solicitud(self, solicitud):
        if solicitud == "cerrar":
            cliente = Cliente("localhost", 8080)
            cliente.cierre()
            respuesta = "Cliente cerrado\n"
            return respuesta.encode()

        try:
            lineas = self.contar_lineas(solicitud)
            caracteres = self.contar_caracteres(solicitud)
            palabras = self.contar_palabras(solicitud)
            respuesta = f"Numero de lineas: {lineas}\n"
            respuesta += f"Numero de caracteres: {caracteres}\n"
            respuesta += f"Numero de palabras: {palabras}\n"
        except FileNotFoundError:
            respuesta = "Fichero no encontrado"

        return respuesta.encode()