require './lib/rondas'

describe Ronda do
  it 'Tiene lista de bolas' do
    bolas = [3, 4]
    ronda = Ronda.new(bolas)
    expect(ronda.bolas).to eq(bolas)
  end

  it 'Guarda la lista de bolas pasada' do
    bolas = [5,1]
    ronda = Ronda.new(bolas)
    expect(ronda.bolas).to eq(bolas)
  end

  it 'No puede tirar más de 10 bolas' do
    bolas = [11, 3]
    expect { Ronda.new(bolas) }.to raise_error(InputError)
  end

  it 'No puede tirar más de 10 bolas de otra forma' do
    bolas = [3, 8]
    expect { Ronda.new(bolas) }.to raise_error(InputError)
  end

  it 'No puede tirar más de 10 bolas último test' do
    bolas = [5, 8]
    expect { Ronda.new(bolas) }.to raise_error(InputError)
  end

  it 'Si recibe más de 10 bolas añade mensaje de error' do
    bolas = [7, 7]
    msg = 'No se puede tirar más de 10 bolas en una ronda'
    expect { Ronda.new(bolas) }.to raise_error(InputError) { |e| expect(e.message).to eq(msg) }
  end

  it 'Sólo puede recibir un array de números' do
    bolas = 'otra cosa'
    msg = 'Las bolas deben ser números entre 0 y 10'
    expect { Ronda.new(bolas) }.to raise_error(InputError) { |e| expect(e.message).to eq(msg) }
  end

  it 'Sólo puede recibir un array de números versión 2' do
    bolas = nil
    msg = 'Las bolas deben ser números entre 0 y 10'
    expect { Ronda.new(bolas) }.to raise_error(InputError) { |e| expect(e.message).to eq(msg) }
  end

  it 'El array recibido sólo puede tener números' do
    bolas = %w[cosa mala]
    msg = 'Las bolas deben ser números entre 0 y 10'
    expect { Ronda.new(bolas) }.to raise_error(InputError) { |e| expect(e.message).to eq(msg) }
  end

  it 'El array recibido sólo puede tener números versión 2' do
    bolas = [nil, [1, 2], true]
    msg = 'Las bolas deben ser números entre 0 y 10'
    expect { Ronda.new(bolas) }.to raise_error(InputError) { |e| expect(e.message).to eq(msg) }
  end

  it 'El array no puede tener más de dos posiciones' do
    bolas = [1, 2, 3]
    msg = 'No se puede tirar más de dos bolas en una ronda'
    expect { Ronda.new(bolas) }.to raise_error(InputError) { |e| expect(e.message).to eq(msg) }
  end

  it 'El array no puede tener cualquier número de posiciones mayores que dos' do
    bolas = Array.new(10, 0)
    msg = 'No se puede tirar más de dos bolas en una ronda'
    expect { Ronda.new(bolas) }.to raise_error(InputError) { |e| expect(e.message).to eq(msg) }
  end

  it 'El array puede tener una única posición si su valor es 10' do
    bolas = [10]
    expect { Ronda.new(bolas) }.not_to raise_error
  end

  it 'El array sólo puede tener una única posición si el número es 10' do
    bolas = [3]
    msg = 'No puede haber una tirada con menos de 2 bolas si la primera no es 10'
    expect { Ronda.new(bolas) }.to raise_error(InputError) { |e| expect(e.message).to eq(msg) }
  end

  it 'El array no puede estar vacío' do
    bolas = []
    msg = 'No puede haber una ronda sin tiradas'
    expect { Ronda.new(bolas) }.to raise_error(InputError) { |e| expect(e.message).to eq(msg) }
  end

  it 'Tiene bonus igual a 0 (número de bolas)' do
    bolas = [3, 6]
    ronda = Ronda.new(bolas)
    expect(ronda.bonus).to eq(0)
  end

  it 'Tiene método para calcular resultado' do
    bolas = [3, 6]
    ronda = Ronda.new(bolas)
    resultado = ronda.resultado
    expect(resultado).to eq(9)
  end

  it 'Calcula el resultado sumando sus bolas' do
    bolas = [7, 0]
    ronda = Ronda.new(bolas)
    resultado = ronda.resultado
    expect(resultado).to eq(7)
  end

  it 'Produce error si recibe más de 0 bolas extra' do
    bolas = [7, 2]
    ronda = Ronda.new(bolas)
    msg = 'Error: se esperaban 0 bolas bonus'
    expect { ronda.resultado([1]) }.to raise_error(InputError) { |e| expect(e.message).to eq(msg) }
  end

  it 'No permite valores de bolas menores que 0' do
    bolas = [-7, 3]
    msg = 'Las bolas deben ser números entre 0 y 10'
    expect { Ronda.new(bolas) }.to raise_error(InputError) { |e| expect(e.message).to eq(msg) }
  end
end

describe Pleno do
  it 'Es una Ronda' do
    expect(Pleno.new).to be_a(Ronda)
  end

  it 'Tiene una sola bola con 10 bolos' do
    pleno = Pleno.new
    expect(pleno.bolas).to eq([10])
  end

  it 'Tiene 2 bolas de bonus' do
    pleno = Pleno.new
    expect(pleno.bonus).to eq(2)
  end

  it 'Para calcular el resultado, toma 2 bolas extra' do
    pleno = Pleno.new
    resultado = pleno.resultado([2,5])
    expect(resultado).to eq(17)
  end

  it 'Para calcular el resultado, toma otras 2 bolas extra' do
    pleno = Pleno.new
    resultado = pleno.resultado([1,1])
    expect(resultado).to eq(12)
  end

  it 'Eleva un error si se proporcionan menos bolas extra de las necesarias' do
    pleno = Pleno.new
    bolas_bonus = [1]
    msg = 'Error: se esperaban 2 bolas bonus'
    expect { pleno.resultado(bolas_bonus) }.to raise_error(InputError) { |e| expect(e.message).to eq(msg) }
  end

  it 'Hay error si no se proporcionan bolas bonus' do
    pleno = Pleno.new
    bolas_bonus = []
    msg = 'Error: se esperaban 2 bolas bonus'
    expect { pleno.resultado(bolas_bonus) }.to raise_error(InputError) { |e| expect(e.message).to eq(msg) }
  end

  it 'Hay error si se proporcionan más de 2 bolas bonus' do
    pleno = Pleno.new
    bolas_bonus = [1,2,4]
    msg = 'Error: se esperaban 2 bolas bonus'
    expect { pleno.resultado(bolas_bonus) }.to raise_error(InputError) { |e| expect(e.message).to eq(msg) }
  end

  it 'Hay error si se proporciona cualquier número de bolas > 2' do
    pleno = Pleno.new
    bolas_bonus = [1,2,4,4,5,6,2,5,6]
    msg = 'Error: se esperaban 2 bolas bonus'
    expect { pleno.resultado(bolas_bonus) }.to raise_error(InputError) { |e| expect(e.message).to eq(msg) }
  end

  it 'Hay un error si no se proporciona un array de enteros' do
    pleno = Pleno.new
    bolas_bonus = [nil, 'jaja']
    msg = 'Las bolas deben ser números entre 0 y 10'
    expect { pleno.resultado(bolas_bonus) }.to raise_error(InputError) { |e| expect(e.message).to eq(msg) }
  end

  it 'El array de bolas bonus no puede tener valores mayores que 10' do
    pleno = Pleno.new
    bolas_bonus = [1, 27]
    msg = 'Las bolas deben ser números entre 0 y 10'
    expect { pleno.resultado(bolas_bonus) }.to raise_error(InputError) { |e| expect(e.message).to eq(msg) }
  end

  it 'Las bolas bonus no pueden ser negativas' do
    bolas_bonus = [3, -10]
    pleno = Pleno.new
    msg = 'Las bolas deben ser números entre 0 y 10'
    expect { pleno.resultado(bolas_bonus) }.to raise_error(InputError) { |e| expect(e.message).to eq(msg) }
  end
end

describe SemiPleno do
  it 'Es una Ronda' do
    bolas = [4, 6]
    semipleno = SemiPleno.new(bolas)
    expect(semipleno).to be_a(Ronda)
  end

  it 'Tiene 1 bola de bonus' do
    bolas = [4, 6]
    semipleno = SemiPleno.new(bolas)
    expect(semipleno.bonus).to eq(1)
  end

  it 'Almacena las bolas' do
    bolas = [4, 6]
    semipleno = SemiPleno.new(bolas)
    expect(semipleno.bolas).to eq(bolas)
  end

  it 'Almacena las bolas correctas' do
    bolas = [5, 5]
    semipleno = SemiPleno.new(bolas)
    expect(semipleno.bolas).to eq(bolas)
  end

  it 'Las bolas suman 10' do
    bolas = [3, 3]
    msg = 'Las bolas de un semipleno deben sumar 10'
    expect { SemiPleno.new(bolas) }.to raise_error(InputError) { |e| expect(e.message).to eq(msg) }
  end

  it 'Para calcular el resultado, toma 1 bola extra' do
    bolas = [3, 7]
    semipleno = SemiPleno.new(bolas)
    resultado = semipleno.resultado([2])
    expect(resultado).to eq(12)
  end

  it 'Para calcular el resultado tiene en cuenta la bola extra' do
    bolas = [7, 3]
    semipleno = SemiPleno.new(bolas)
    resultado = semipleno.resultado([9])
    expect(resultado).to eq(19)
  end

  it 'El array de bolas bonus no puede tener más de una posición' do
    bolas = [7, 3]
    semipleno = SemiPleno.new(bolas)
    bolas_bonus = [10, 3]
    msg = 'Error: se esperaban 1 bolas bonus'
    expect { semipleno.resultado(bolas_bonus) }.to raise_error(InputError) { |e| expect(e.message).to eq(msg) }
  end

  it 'El array de bolas bonus no puede tener más de una posición (triangulación)' do
    bolas = [7, 3]
    semipleno = SemiPleno.new(bolas)
    bolas_bonus = []
    msg = 'Error: se esperaban 1 bolas bonus'
    expect { semipleno.resultado(bolas_bonus) }.to raise_error(InputError) { |e| expect(e.message).to eq(msg) }
  end

  it 'Hay un error si no se proporciona un array de enteros' do
    bolas = [7, 3]
    semipleno = SemiPleno.new(bolas)
    bolas_bonus = ['jaja']
    msg = 'Las bolas deben ser números entre 0 y 10'
    expect { semipleno.resultado(bolas_bonus) }.to raise_error(InputError) { |e| expect(e.message).to eq(msg) }
  end

  it 'El array de bolas extra no puede tener valores mayores que 10' do
    bolas = [7, 3]
    semipleno = SemiPleno.new(bolas)
    bolas_bonus = [11]
    msg = 'Las bolas deben ser números entre 0 y 10'
    expect { semipleno.resultado(bolas_bonus) }.to raise_error(InputError) { |e| expect(e.message).to eq(msg) }
  end

  it 'No puede recibir bolas menores de 0' do
    bolas = [13, -3]
    msg = 'Las bolas deben ser números entre 0 y 10'
    expect { SemiPleno.new(bolas) }.to raise_error(InputError) { |e| expect(e.message).to eq(msg) }
  end

  it 'Las bolas bonus no pueden ser negativas' do
    bolas_bonus = [-3]
    semipleno = SemiPleno.new([6, 4])
    msg = 'Las bolas deben ser números entre 0 y 10'
    expect { semipleno.resultado(bolas_bonus) }.to raise_error(InputError) { |e| expect(e.message).to eq(msg) }
  end
end

