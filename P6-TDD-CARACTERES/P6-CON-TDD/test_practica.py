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
            file.write("hola soy gon")

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

    def test_leer_archivo_no_encontrado(self):
        manager = Manager()
        solicitud = self.archivo_no_encontrado
        respuesta = manager.gestionar_solicitud(solicitud)
        assert respuesta == b"Fichero no encontrado"

    def test_leer_archivo_existente_con_contenido(self):
        manager = Manager()
        solicitud = self.archivo_existente
        respuesta = manager.gestionar_solicitud(solicitud)
        lineas_esperadas = 1
        caracteres_esperados = 12
        palabras_esperadas = 3  # Se corrige el valor esperado
        respuesta_esperada = f"Numero de lineas: {lineas_esperadas}\n"
        respuesta_esperada += f"Numero de caracteres: {caracteres_esperados}\n"
        respuesta_esperada += f"Numero de palabras: {palabras_esperadas}\n"
        assert respuesta == respuesta_esperada.encode()


    def test_leer_archivo_vacio(self):
        manager = Manager()
        solicitud = self.archivo_vacio
        respuesta = manager.gestionar_solicitud(solicitud)
        respuesta_esperada = "Numero de lineas: 0\nNumero de caracteres: 0\nNumero de palabras: 0\n"
        assert respuesta == respuesta_esperada.encode()
    
    def test_contar_lineas(self):
        manager = Manager()
        solicitud = self.archivo_existente # Nombre de un archivo existente con contenido
        lineas_esperadas = 1
        lineas_obtenidas = manager.contar_lineas(solicitud)
        assert lineas_obtenidas == lineas_esperadas


    def test_contar_caracteres(self):
        manager = Manager()
        solicitud = self.archivo_existente  # Nombre de un archivo existente con contenido
        caracteres_esperados = 12
        caracteres_obtenidos = manager.contar_caracteres(solicitud)
        assert caracteres_obtenidos == caracteres_esperados


    def test_contar_palabras(self):
        manager = Manager()
        solicitud = self.archivo_existente  # Nombre de un archivo existente con contenido
        palabras_esperadas = 3
        palabras_obtenidas = manager.contar_palabras(solicitud)
        assert palabras_obtenidas == palabras_esperadas



