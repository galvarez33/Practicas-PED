class Rectangulo:

    def __init__(self, punto1, punto2):
        if isinstance(punto1, tuple) and isinstance(punto2, tuple):
                self.punto1 = punto1
                self.punto2 = punto2
        else:
            raise ValueError("Formato de punto incorrecto")

    def crear_puntos(self):
        if self.punto1 != self.punto2 and self.punto1[0] != self.punto2[0] and self.punto1[1] != self.punto2[1]  :
            punto3 = (self.punto2[0], self.punto1[1])
            punto4 = (self.punto1[0], self.punto2[1])
            print(f"\nLos puntos generados: p3{punto3}, p4{punto4}")
            return punto3, punto4
        else:
            raise ValueError("Has pasado dos puntos iguales o 2 x iguales o dos y iguales")
        
    def crear_rectangulo(self):
        punto3, punto4 = self.crear_puntos()
        l = [self.punto1,self.punto2, punto3, punto4]
        print(f"\nEl rectangulo generado es : p1{self.punto1} y p3{punto3} como base y como altura p4{punto4} y p2{self.punto2}")
        return l
    
    def calcular_area(self):
        base = self.punto2[0]- self.punto1[0]
        altura = self.punto2[1]- self.punto1[1]
        area = base * altura
        print(f"\nel area del rectangulo seria: {area}")
        return area 
    
    def calcular_perimetro(self):
        perimetro = (self.punto2[0]- self.punto1[0])*2 + (self.punto2[1]- self.punto1[1])*2
        print(f"\nel perimetro del rectangulo seria: {perimetro}")
        return perimetro
    
    def intersecta_con(self, otro_rectangulo):

        x3, y3 = otro_rectangulo[0]
        x4, y4 = otro_rectangulo[1]

        if (self.punto2[0] < x3 or x4 < self.punto1[0]) or (self.punto2[1] < y3 or y4 < self.punto1[1]):
            print("\nlos rectanguloa NO se intersectan !!!!")
            return False  
        
        else:
            print("\n Los rectangulos se Intersecan !!!")
            return True 
        
if __name__ == "__main__":
    p1 = input("introduzca p1 en formato tupla:")
    p2 = input("introduzca p2 en formato tupla:")
    p1 = tuple(map(int, p1.strip('()').split(',')))  # Convertir cadena a tupla de enteros
    p2 = tuple(map(int, p2.strip('()').split(',')))

    
    p3 = input("introduzca p1 del rectangulo 2 en formato tupla:")
    p4 = input("introduzca p2 del rectangulo 2 en formato tupla:")
    p3 = tuple(map(int, p3.strip('()').split(',')))  # Convertir cadena a tupla de enteros
    p4 = tuple(map(int, p4.strip('()').split(',')))

    r = Rectangulo(p1, p2)
    r.crear_puntos()
    r.crear_rectangulo()
    r.calcular_area()
    r.calcular_perimetro()
    otro_rectangulo = (p3, p4)
    r.intersecta_con(otro_rectangulo)
    
    
    
        
        