from rectangulo import Rectangulo

def test_guarda_punto1():
    punto1 = (2,3)
    punto2 = (2,3)
    obj = Rectangulo(punto1, punto2)
    assert obj.punto1 == punto1

def test_guarda_punto2():
    punto1 = (2,3)
    punto2 = (2,3)
    obj = Rectangulo(punto1, punto2)
    assert obj.punto2 == punto2

def test_punto1_debe_ser_tupla():
    punto1 = (3)
    punto2 = (2,3)
    try:
        obj = Rectangulo(punto1, punto2)
        isinstance(obj.punto1, tuple)
        assert False
    except ValueError:
        assert True

def test_punto2_debe_ser_tupla():
    punto1 = (3,2)
    punto2 = (2)
    try:
        obj = Rectangulo(punto1, punto2)
        isinstance(obj.punto2, tuple)
        assert False
    except ValueError:
        assert True


def test_crear_p3_y_p4_rectangulo():
    punto1 = (1,1)
    punto2 = (3,2)
    obj = Rectangulo(punto1, punto2)
    p3 = (3, 1)
    p4 =(1, 2)
   
    assert obj.crear_puntos() == (p3, p4)

def test_guarda_puntos_lista():
    punto1 = (1,1)
    punto2 = (3,2)
    obj = Rectangulo(punto1, punto2)
    puntos = obj.crear_rectangulo()
    assert puntos == [(1,1),(3,2),(3,1),(1,2)]

def test_area_rectangulo():
    punto1 = (1, 1)
    punto2 = (3, 4)
    obj = Rectangulo(punto1, punto2)
    area = obj.calcular_area()
    assert area == 6

def test_area_rectangulo2():
    punto1 = (1, 1)
    punto2 = (2, 3)
    obj = Rectangulo(punto1, punto2)
    area = obj.calcular_area()
    assert area == 2

def test_area_rectangulo_negaitvo():
    punto1 = (-1, -1)
    punto2 = (-3, -2)
    obj = Rectangulo(punto1, punto2)
    area = obj.calcular_area()
    assert area == 2

def test_area_rectangulo_decimales():
    punto1 = (1.5, 2.5)
    punto2 = (3.5, 4.5)
    obj = Rectangulo(punto1, punto2)
    area = obj.calcular_area()
    assert area == 4.0

def test_caso_error_p1_p2_iguales():
    punto1 = (1,1)
    punto2 = (1,1)
    try:
        obj = Rectangulo(punto1,punto2).crear_puntos()
        assert False
    except ValueError:
        assert True 

def test_caso_p1_mayor_que_p2():
    punto1 = (2,1)
    punto2 = (0,0)
    obj = Rectangulo(punto1, punto2)
    area = obj.calcular_area()
    assert area == 2

def test_calcular_perimetro():
    punto1 = (0,0)
    punto2 = (2,1)
    obj = Rectangulo(punto1, punto2)
    area = obj.calcular_perimetro()
    assert area == 6

def test_calcular_perimetro():
    punto1 = (1,1)
    punto2 = (4,2)
    obj = Rectangulo(punto1, punto2)
    area = obj.calcular_perimetro()
    assert area == 8

def test_rectangulo_con_linea_horizontal():
    punto1 = (1, 1)
    punto2 = (4, 1)
    try:
        obj = Rectangulo(punto1, punto2).crear_puntos()
        assert False  
    except ValueError:
        assert True  

def test_rectangulo_con_linea_vertical():
    punto1 = (1, 1)
    punto2 = (1, 4)
    try:
        obj = Rectangulo(punto1, punto2).crear_puntos()
        assert False  
    except ValueError:
        assert True  

def test_rectangulos_se_intersectan():
    punto1_r1 = (1, 1)
    punto2_r1 = (4, 3)
    rectangulo1 = Rectangulo(punto1_r1, punto2_r1)

    punto1_r2 = (2, 2)
    punto2_r2 = (5, 4)
    rectangulo2 = (punto1_r2, punto2_r2)
    

    assert rectangulo1.intersecta_con(rectangulo2) == True

def test_rectangulos_no_se_intersectan():
    rectangulo1 = Rectangulo((1, 1), (3, 4))
    punto1_r2 = (5, 5)
    punto2_r2 = (7, 8)
    rectangulo2 = (punto1_r2, punto2_r2)

    assert rectangulo1.intersecta_con(rectangulo2) == False




