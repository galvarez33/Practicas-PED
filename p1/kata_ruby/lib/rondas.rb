require 'validadores'

class Ronda
  # Getter para bolas
  attr_reader :bolas, :bonus

  # Constructor
  def initialize(bolas)
    @bolas = bolas
    @bonus = 0

    # Comprueba condiciones de error
    [ValidadorValores.new, ValidadorLongitudRonda.new, Validador10oMenosBolas.new].each { |v| v.validar(bolas) }
  end

  def resultado(bolas_bonus = [])
    # Comprueba condiciones de error
    ValidadorValores.new.validar(bolas_bonus)
    ValidadorLongitudBolasBonus.new.validar(bolas_bonus, @bonus)

    # Calcula resultado
    @bolas.sum + bolas_bonus.sum
  end
end

class Pleno < Ronda
  def initialize
    super([10])
    @bonus = 2
  end
end

class SemiPleno < Ronda
  def initialize(bolas)
    super(bolas)
    @bonus = 1

    raise InputError, 'Las bolas de un semipleno deben sumar 10' unless @bolas.sum == 10
  end
end
