from suma_recursiva import SumaRecursiva


def test_crear_valor():
    valor = 3
    objeto = SumaRecursiva(valor)

    assert objeto.valor == valor

def test_suma_recursiva():
    n = 5
    resultado_esperado = 15 #1+2+3+4+5
    sumador = SumaRecursiva(n)
    resultado = sumador.suma_recursiva()

    assert resultado_esperado == resultado

def test_suma_recursiva2():
    n = 6
    resultado_esperado = 21 #1+2+3+4+5+6
    sumador = SumaRecursiva(n)
    resultado = sumador.suma_recursiva()

    assert resultado_esperado == resultado

def test_suma_recursiva3():
    n = 3
    resultado_esperado = 6 #1+2+3
    sumador = SumaRecursiva(n)
    resultado = sumador.suma_recursiva()

    assert resultado_esperado == resultado

def test_valor_no_entero():
    sumador = SumaRecursiva(3.25)
    try:
        sumador.suma_recursiva()
        assert False, "se esperaba que fallase"
    except ValueError:
        assert True

def test_valor_entero_negativo():
    sumador = SumaRecursiva(-4)
    try:
        sumador.suma_recursiva()
        assert False, "se esperaba que fallase"
    except ValueError:
        assert True