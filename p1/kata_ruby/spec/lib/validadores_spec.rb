require 'validadores'
require 'errors'

describe Validador do
  it "Tiene método abstracto 'validar'" do
    validador = Validador.new
    expect { validador.validar('test') }.to raise_error(NotImplementedError)
  end

  it 'validar toma cualquier número de argumentos' do
    validador = Validador.new
    expect { validador.validar('test', nil, 8) }.to raise_error(NotImplementedError)
  end
end

describe ValidadorValores do
  it 'Es subclase de validador' do
    validador = ValidadorValores.new
    expect(validador).to be_a(Validador)
  end

  it 'Implementa el método validar' do
    validador = ValidadorValores.new
    expect { validador.validar([0, 1]) }.not_to raise_error
  end
end

describe ValidadorLongitudRonda do
  it 'Es subclase de validador' do
    validador = ValidadorLongitudRonda.new
    expect(validador).to be_a(Validador)
  end

  it 'Implementa el método validar' do
    validador = ValidadorLongitudRonda.new
    expect { validador.validar([0, 1]) }.not_to raise_error
  end
end

describe ValidadorLongitudBolasBonus do
  it 'Es subclase de validador' do
    validador = ValidadorLongitudBolasBonus.new
    expect(validador).to be_a(Validador)
  end

  it 'Implementa el método validar' do
    validador = ValidadorLongitudBolasBonus.new
    expect { validador.validar([0, 1], 2) }.not_to raise_error
  end
end

describe Validador10oMenosBolas do
  it 'Es sublcase de validador' do
    validador = Validador10oMenosBolas.new
    expect(validador).to be_a(Validador)
  end

  it 'Implementa el método validar' do
    validador = Validador10oMenosBolas.new
    expect { validador.validar([0, 1]) }.not_to raise_error
  end
end
