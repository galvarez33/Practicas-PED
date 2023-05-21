from suma_dos_numero import SumaDosNumeros


def test_suma_dos_numeros():
    sumar = SumaDosNumeros(2,3)
    resultado = sumar.suma() 
    assert resultado == 5

def test_suma_dos_numeros_a_erroneo():
    a = "hola"
    b = 3
    try:
        SumaDosNumeros(a,b).suma()
        assert False, "Se esperaba excepcion"
    except ValueError:
        assert True

def test_suma_dos_numeros_b_erroneo():
    a = 2
    b = "hola"
    try:
        SumaDosNumeros(a,b).suma()
        assert False, "Se esperaba excepcion"
    except ValueError:
        assert True

def test_suma_numeros_negativos():
    assert SumaDosNumeros(-2,-3).suma() == -5

def test_suma_dos_numeros_decimales():
    assert SumaDosNumeros(12.5, 7.5).suma() == 20

def test_guarda_primer_valor():
    a = 1
    b = 2
    resultado = SumaDosNumeros(a,b)
    assert resultado.a == a

def test_guarda_segundo_valor():
    a = 1
    b = 2
    resultado = SumaDosNumeros(a,b)
    assert resultado.b == b
   