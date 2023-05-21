
class SumaDosNumeros:
    def __init__(self, a, b):
       self.a = a
       self.b = b


    def es_entero(self):
       try:
          float(self.a)
          float(self.b)
          return True
       except:
          return False


    def suma(self):
        if not self.es_entero():
           raise ValueError("Valor no valido")

        a = float(self.a)
        b = float(self.b)
        return a + b 
    
           
        