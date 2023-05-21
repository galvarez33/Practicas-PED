
class SumaRecursiva:
    
    def __init__(self, valor):
        self.valor = valor
    
    def validacion(self):
        if not isinstance(self.valor, int):
            raise ValueError("El valor no es un entero")
        if self.valor < 0:
            raise ValueError("El valor es negativo")


    def suma_recursiva(self):
        self.validacion()
        if self.valor == 0:
            return 0
        else:
            return self.valor + SumaRecursiva(self.valor -1).suma_recursiva()