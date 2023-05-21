import os
from manager import Manager

class TestManager:
    archivo_existente = "archivo_existente.txt"
    archivo_vacio = "archivo_vacio.txt"
    archivo_no_encontrado = "archivo_no_encontrado.txt"
    archivo_binario = "archivo_binario.bin"

    def setup_method(self, method):
        # Crear el archivo existente
        with open(self.archivo_existente, 'w') as file:
            file.write("Contenido del archivo existente")

        # Crear el archivo vacío
        open(self.archivo_vacio, 'w').close()

        # Crear el archivo binario
        with open(self.archivo_binario, 'wb') as file:
            file.write(b"\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09")

    def teardown_method(self, method):
        # Borrar los archivos creados
        os.remove(self.archivo_existente)
        os.remove(self.archivo_vacio)
        os.remove(self.archivo_binario)

    def test_cerrar_cliente(self):
        manager = Manager()
        solicitud = "cerrar"
        respuesta = manager.gestionar_solicitud(solicitud)
        assert respuesta == b"Cliente cerrado\n"

    def test_leer_archivo_vacio(self):
        manager = Manager()
        solicitud = self.archivo_vacio
        contenido_esperado = b""
        respuesta = manager.gestionar_solicitud(solicitud)
        assert respuesta == contenido_esperado

    def test_leer_archivo_no_encontrado(self):
        manager = Manager()
        solicitud = self.archivo_no_encontrado
        respuesta = manager.gestionar_solicitud(solicitud)
        assert respuesta == b"Fichero no encontrado"

    def test_leer_archivo_binario(self):
        manager = Manager()
        solicitud = self.archivo_binario
        contenido_esperado = b"\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09"
        respuesta = manager.gestionar_solicitud(solicitud)
        assert respuesta == contenido_esperado
