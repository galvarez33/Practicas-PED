from dni import Dni

def test_store_dni():
    dni = "12345678N"
    obj = Dni(dni)
    assert obj.dni == dni

def test_comrpobar_longitud():
    dni = "12345678N"
    assert Dni(dni).validar_long() == 9

def test_longitud_erronea():
    dni = "12345678"
    try:
        Dni(dni).validar_long()
        assert False, "No deberia pasar"
    except ValueError:
        assert True

def test_validar_formato_letra():
    dni = "12345678N"
    obj = Dni(dni)
    assert obj.validar_formato() == True

def test_formato_letra_erroneo():
    dni = "12345678"
    try:
        Dni(dni).validar_formato()
        assert False, "No deberia pasar"
    except SyntaxError:
        assert True

def test_formato_numero_erroneo():
    dni = "1234n67N"
    try:
        Dni(dni).validar_formato()
        assert False, "No deberia pasar"
    except SyntaxError:
        assert True


def test_validar_calculo():
    dni = "12345678Z"
    obj = Dni(dni)
    assert obj.validar_calculo() == dni

def test_validar_calculo():
    dni = "02454678A"
    obj = Dni(dni)
    assert obj.validar_calculo() == dni


