import pytest
from partida import Partida

class TestPartida:

    def test_crear_partida_con_tupla_valida(self):
        partida = Partida()
        partida.crear_partida([(1, 2)] * 10)
        assert partida.rondas == [(1, 2)] * 10


    def test_crear_partida_con_tupla_valida_y_muchos_valores(self):
        partida = Partida()
        rondas = [(0, 0)] * 10
        rondas.append((0, 0))
        with pytest.raises(ValueError):
            partida.crear_partida(rondas)


    def test_crear_partida_con_tupla_invalida(self):
        partida = Partida()
        with pytest.raises(ValueError):
            partida.crear_partida([1, 2])

    def test_crear_partida_con_tupla_invalida_con_1_valor(self):
        partida = Partida()
        with pytest.raises(ValueError):
            partida.crear_partida([(1,)])

    def test_crear_partida_con_tupla_invalida_con_valor_no_entero(self):
        partida = Partida()
        with pytest.raises(ValueError):
            partida.crear_partida([(1, "2")])

    def test_crear_partida_con_tupla_invalida_con_4_valores(self):
        partida = Partida()
        with pytest.raises(ValueError):
            partida.crear_partida([(1, 2, 3)])
    
    def test_crear_partida_con_menos_de_10_rondas(self):
        partida = Partida()
        with pytest.raises(ValueError):
            partida.crear_partida([(0, 0)] * 9)

    def test_crear_partida_con_tupla_invalida(self):
        partida = Partida()
        with pytest.raises(ValueError):
            partida.crear_partida([1, 2])
    
    def test_puntuacion_total_con_partida_vacia(self):
        partida = Partida()
        assert partida.puntuacion_total() is None
  
    def test_puntuacion_total_con_partida_con_puntuacion_0(self):
        partida = Partida()
        partida.crear_partida([(0, 0)] * 10)
        assert partida.puntuacion_total() == 0

    def test_es_strike_en_la_ultima_ronda(self):
        partida = Partida()
        partida.crear_partida([(0, 0)] * 9 + [(10, 10, 10)])
        assert partida.es_strike(9)
        assert not partida.es_strike(8)

    def test_puntuacion_spare_en_ultima_ronda(self):
            partida = Partida()
            partida.crear_partida([(0, 0)] * 9 + [(5, 5, 5)])
            assert partida.puntuacion_spare(9) == 15

    def test_puntuacion_total_con_varias_rondas(self):
        partida = Partida()
        partida.crear_partida([(0, 0), (1, 2), (10, 0), (5, 5), (7, 1), (9, 1), (0, 10), (3, 3), (6, 2), (10, 10, 10)])
        assert partida.puntuacion_total() == 115

    def test_puntuacion_total_con_2_strikes_seguidos(self):
        partida = Partida()
        partida.crear_partida([(10, 0), (10, 0), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)])
        assert partida.puntuacion_total() == 49

    def test_puntuacion_total_con_3_strikes_seguidos(self):
        partida = Partida()
        partida.crear_partida([(10, 0), (10, 0), (10, 0), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)])
        assert partida.puntuacion_total() == 77

    def test_puntuacion_total_con_todo_strikes(self):
        partida = Partida()
        partida.crear_partida([(10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10,10,10)])
        assert partida.puntuacion_total() == 300


    def test_puntuacion_total_con_4_strikes(self):
        partida = Partida()
        partida.crear_partida([(10, 0), (10, 0), (10, 0), (10, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)])
        assert partida.puntuacion_total() == 90

    def test_puntuacion_total_con_5_strikes(self):
        partida = Partida()
        partida.crear_partida([(10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (0,0)])
        assert partida.puntuacion_total() == 240

    def test_puntuacion_total_con_todo_spares(self):
        partida = Partida()
        partida.crear_partida([(0, 10), (0, 10), (0, 10), (0, 10), (0, 10), (0, 10), (0, 10), (0, 10), (0, 10), (0, 10, 10)])
        assert partida.puntuacion_total() == 110

    def test_puntuacion_total_con_bonus_con_strike(self):
        partida = Partida()
        partida.crear_partida([(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (10, 8)])
        assert partida.puntuacion_total() == 18
    
    def test_puntuacion_total_con_bonus_con_spare(self):
        partida = Partida()
        partida.crear_partida([(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (9, 1, 7)])
        assert partida.puntuacion_total() == 17

    def test_puntuacion_total_con_bonus_sin_strike_ni_spare(self):
        partida = Partida()
        partida.crear_partida([(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (8, 1)])
        assert partida.puntuacion_total() == 9
 
    












