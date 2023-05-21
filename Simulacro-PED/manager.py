import time


class Manager:
    def gestionar_solicitud(self, solicitud):
        if solicitud.lower() == 'hora':
            hora = time.strftime('%H:%M:%S') + '\n'
                               
            return hora
        elif solicitud.lower() == 'fecha':
            fecha = time.strftime('%Y-%m-%d')
            return fecha
        else:
            mensaje_error = "Valor inválido"
            return mensaje_error
