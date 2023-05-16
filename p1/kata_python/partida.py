class Partida:
    
    def __init__(self):
        self.rondas = []

    def crear_partida(self, rondas):
     if len(rondas) != 10:
        raise ValueError("Se deben pasar exactamente 10 rondas")
     for ronda in rondas:
        if not isinstance(ronda, tuple) or len(ronda) < 2 or len(ronda) > 3:
            raise ValueError("Las rondas deben ser tuplas con 2 o 3 valores enteros")
        for lanzamiento in ronda:
            if not isinstance(lanzamiento, int):
                raise ValueError("Los tiros deben ser enteros")
     self.rondas = rondas



    def puntuacion_total_con_partida_vacia(self):
        partida = Partida()
        assert partida.puntuacion_total() is None
	
    def es_strike(self, i):
        return i < len(self.rondas) and self.rondas[i][0] == 10


    def es_spare(self, i):
        return sum(self.rondas[i]) == 10 and self.rondas[i][0] != 10


    def puntuacion_strike(self, i):
       if i == 9:
            return sum(self.rondas[i])
       else:
            puntuacion = 10
            if self.es_strike(i + 1):
                puntuacion += 10
                if i + 2 <= 9:
                    puntuacion += self.rondas[i + 2][0]
            else:
                puntuacion += self.puntuacion_ronda(i + 1)
            return puntuacion


    def puntuacion_spare(self, i):
        if i == 9:
            return sum(self.rondas[i])
        else:
            puntuacion = 10 + self.rondas[i + 1][0]
            if self.es_strike(i + 1):
                puntuacion += 10
            return puntuacion


    def puntuacion_ronda(self, i):
        return sum(self.rondas[i])


    def puntuacion_total(self):
        if not self.rondas or len(self.rondas) < 10:
            return None
        puntuacion = 0
        i = 0
        for _ in range(10):
            if self.es_strike(i):
                puntuacion += self.puntuacion_strike(i)
                i += 1
            elif self.es_spare(i):  
                puntuacion += self.puntuacion_spare(i)
                i += 1
            else:
                puntuacion += self.puntuacion_ronda(i)
                i += 1
        return puntuacion
