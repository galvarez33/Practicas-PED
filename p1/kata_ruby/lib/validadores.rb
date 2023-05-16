class Validador
  def validar(*args)
    raise NotImplementedError
  end
end

class ValidadorValores < Validador
  def validar(bolas)
    valores_validos = (es_array_de_enteros?(bolas) and valores_entre_0_y_10?(bolas))
    raise InputError, 'Las bolas deben ser números entre 0 y 10' unless valores_validos
  end

  private

  def es_array_de_enteros?(bolas)
    bolas.is_a? Array and bolas.all? {|x| x.is_a? Integer }
  end

  def valores_entre_0_y_10?(bolas)
    bolas.all? { |bola| bola.between?(0, 10) }
  end
end

class ValidadorLongitudRonda < Validador
  def validar(bolas)
    if bolas.size > 2
      raise InputError, 'No se puede tirar más de dos bolas en una ronda'
    elsif bolas.size == 1 and bolas.first != 10
      raise InputError, 'No puede haber una tirada con menos de 2 bolas si la primera no es 10'
    elsif bolas.empty?
      raise InputError, 'No puede haber una ronda sin tiradas'
    end
  end
end

class ValidadorLongitudBolasBonus < Validador
  def validar(bolas, longitud)
    longitud_adecuada = bolas.size == longitud
    raise InputError, "Error: se esperaban #{longitud} bolas bonus" unless longitud_adecuada
  end
end

class Validador10oMenosBolas < Validador
  def validar(bolas)
    tira_numero_valido = bolas.sum <= 10
    raise InputError, 'No se puede tirar más de 10 bolas en una ronda' unless tira_numero_valido
  end
end
