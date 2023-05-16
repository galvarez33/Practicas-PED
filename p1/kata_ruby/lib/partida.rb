class Partida
  def initialize(rondas, bolas_extra = [])
    ValidadorValores.new.validar(bolas_extra)
    ValidadorLongitudBolasBonus.new.validar(bolas_extra, rondas.last.bonus)

    @cola_rondas = rondas
    @cola_bolas = []

    rondas.map { |ronda| @cola_bolas << ronda.bolas }
    @cola_bolas << bolas_extra

    @cola_bolas.flatten!
  end

  def resultado
    sum = 0

    until @cola_rondas.empty? do
      ronda = @cola_rondas.shift

      bolas_a_descartar = ronda.bolas.size
      @cola_bolas.shift(bolas_a_descartar)

      bolas_bonus = @cola_bolas.first(ronda.bonus)
      sum += ronda.resultado(bolas_bonus)
    end

    sum
  end
end
