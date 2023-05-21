import pytest
from manager import Manager

@pytest.fixture
def manager():
    return Manager()

def test_gestionar_solicitud_hora(manager):
    resultado = manager.gestionar_solicitud('hora')
    assert isinstance(resultado, str)

def test_verifica_len_hora(manager):
    resultado = manager.gestionar_solicitud('hora')
    assert len(resultado) == 9  # Verificar el formato HH:MM:SS + '\n'

def test_gestionar_solicitud_fecha(manager):
    resultado = manager.gestionar_solicitud('fecha')
    assert isinstance(resultado, str)
    assert len(resultado) == 10  # Verificar el formato YYYY-MM-DD

def test_gestionar_solicitud_hora_insensible(manager):
    resultado = manager.gestionar_solicitud('HoRa')  # Probar mayúsculas y minúsculas mixtas
    assert isinstance(resultado, str)
    assert len(resultado) == 9

def test_gestionar_solicitud_fecha_insensible(manager):
    resultado = manager.gestionar_solicitud('FeChA')  # Probar mayúsculas y minúsculas mixtas
    assert isinstance(resultado, str)
    assert len(resultado) == 10

def test_gestionar_solicitud_invalida(manager):
    resultado = manager.gestionar_solicitud('foo')
    assert resultado == 'Valor inválido'
    
   


