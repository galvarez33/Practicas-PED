require 'partida'

describe Partida do
  it 'Calcula el resultado de una lista de rondas' do
    rondas = Array.new(10, Ronda.new([0, 0]))
    partida = Partida.new(rondas)

    expect(partida.resultado).to eq(0)
  end

  it 'Calcula el verdadero resultado de las rondas recibidas' do
    rondas = Array.new(10, Ronda.new([1, 2]))
    partida = Partida.new(rondas)

    expect(partida.resultado).to eq(30)
  end

  it 'Calcula el resultado con plenos y semiplenos' do
    rondas = [Ronda.new([1, 1]), Pleno.new, SemiPleno.new([5, 5]), Ronda.new([7, 1])]
    rondas.concat(Array.new(6, Ronda.new([0, 0])))
    partida = Partida.new(rondas)

    expect(partida.resultado).to eq(2 + (10 + 5 + 5) + (5 + 5 + 7) + 7 + 1)
  end

  it 'Calcula el resultado con otros plenos y semiplenos' do
    rondas = [Pleno.new, Ronda.new([4, 5]), Ronda.new([0, 0]), SemiPleno.new([7, 3]), Ronda.new([1, 8])]
    rondas.concat(Array.new(5, Ronda.new([0, 0])))
    partida = Partida.new(rondas)

    expect(partida.resultado).to eq((10 + 4 + 5) + (4 + 5) + 0 + (7 + 3 + 1) + (1 + 8))
  end

  it 'Calcula el resultado con semipleno al final' do
    rondas = Array.new(9, Ronda.new([0, 0]))
    rondas.concat([SemiPleno.new([9, 1])])
    bolas_extra = [6]
    partida = Partida.new(rondas, bolas_extra)

    expect(partida.resultado).to eq(9 + 1 + 6)
  end

  it 'Calcula el resultado con otra bola semipleno al final' do
    rondas = Array.new(9, Ronda.new([0, 0]))
    rondas.concat([SemiPleno.new([9, 1])])
    bolas_extra = [8]
    partida = Partida.new(rondas, bolas_extra)

    expect(partida.resultado).to eq(9 + 1 + 8)
  end

  it 'Calcula el resultado con pelno al final' do
    rondas = Array.new(9, Ronda.new([0, 0]))
    rondas.concat([Pleno.new])
    bolas_extra = [8, 1]
    partida = Partida.new(rondas, bolas_extra)

    expect(partida.resultado).to eq(10 + 8 + 1)
  end

  it 'Calcula el resultado con pelno al final' do
    rondas = Array.new(9, Ronda.new([0, 0]))
    rondas.concat([Pleno.new])
    bolas_extra = [6, 4]
    partida = Partida.new(rondas, bolas_extra)

    expect(partida.resultado).to eq(10 + 6 + 4)
  end

  it 'Las bolas extra son un array de enteros' do
    rondas = Array.new(9, Ronda.new([0, 0]))
    rondas.concat([Pleno.new])
    bolas_extra = [nil, 'hola']

    msg = 'Las bolas deben ser números entre 0 y 10'
    expect { Partida.new(rondas, bolas_extra) }.to raise_error(InputError) { |e| expect(e.message).to eq(msg)}
  end

  it 'No puede recibir más de 2 bolas extra para un pleno' do
    rondas = Array.new(9, Ronda.new([0, 0]))
    rondas.concat([Pleno.new])
    bolas_extra = [1, 3, 4]

    msg = 'Error: se esperaban 2 bolas bonus'
    expect { Partida.new(rondas, bolas_extra) }.to raise_error(InputError) { |e| expect(e.message).to eq(msg)}
  end

  it 'No puede recibir ningún número superior a 2 bolas bonus' do
    rondas = Array.new(9, Ronda.new([0, 0]))
    rondas.concat([Pleno.new])
    bolas_extra = [1, 3, 4, 5, 6, 7]

    msg = 'Error: se esperaban 2 bolas bonus'
    expect { Partida.new(rondas, bolas_extra) }.to raise_error(InputError) { |e| expect(e.message).to eq(msg)}
  end

  it 'Sólo puede recibir 1 bola extra si es un semipleno' do
    rondas = Array.new(9, Ronda.new([0, 0]))
    rondas.concat([SemiPleno.new([1, 9])])
    bolas_extra = [1, 3]

    msg = 'Error: se esperaban 1 bolas bonus'
    expect { Partida.new(rondas, bolas_extra) }.to raise_error(InputError) { |e| expect(e.message).to eq(msg)}
  end
end
