from rectangulo import Rectangulo

def test_constructor_altura():
    a = 2
    b = 2
    r = Rectangulo(a, b)
    assert r.a == a  

def test_constructor_base():
    a = 2
    b = 2
    r = Rectangulo(a, b)
    assert r.b == b

def test_calcular_area():
    a = 2
    b = 2
    r = Rectangulo(a,b).area()
    assert r == 4

def test_calcular_area2():
    a = 3
    b = 2
    r = Rectangulo(a,b).area()
    assert r == 6

def test_calcular_area3():
    a = 3
    b = 3
    r = Rectangulo(a,b).area()
    assert r == 9

def test_calcular_area_con_negativo():
    a = -3
    b = 3
    try:
        Rectangulo(a,b).area()
        assert False, "Debe fallar"
    except ValueError:
        assert True

def test_calcular_perimetro():
    assert Rectangulo(2, 3).perimetro() == 10

def test_calcular_perimetro():
    assert Rectangulo(3, 4).perimetro() == 14

def test_calcular_perimetro():
    assert Rectangulo(1, 2).perimetro() == 6

def test_perimetro_negativo():
    try:
        Rectangulo(-2,1).perimetro()
        assert False,"debe fallar"
    except ValueError:
        assert True

def test_ejecutar_programa_que_muestre_area_y_perimetro():
    altura = 2
    base = 3
    r = Rectangulo(altura, base)
    r.ejecutar()
    assert True

