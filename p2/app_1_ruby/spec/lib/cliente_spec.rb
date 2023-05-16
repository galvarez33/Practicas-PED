require 'cliente'

describe Cliente do
  describe 'initialize()' do
    it 'guarda el pipe de lectura recibido' do
      read, write = IO.pipe
      cliente = Cliente.new(read, write)
      expect(cliente.instance_variable_get(:@read)).to be(read)
    end

    it 'guarda el pipe de escritura recibido' do
      read, write = IO.pipe
      cliente = Cliente.new(read, write)
      expect(cliente.instance_variable_get(:@write)).to be(write)
    end

    it 'lanza excepción si no recibe un objeto IO como pipe de lectura' do
      read, write = IO.pipe
      read = 'Jaja'
      msg = 'Error, se esperaba un Pipe'
      expect { Cliente.new(read, write) }.to raise_error(TypeError) { |e| expect(e.message).to eq(msg) }
    end

    it 'lanza excepción si recibe cualquier objecto exceptio un objeto IO como pipe de lectura' do
      read, write = IO.pipe
      read = nil
      msg = 'Error, se esperaba un Pipe'
      expect { Cliente.new(read, write) }.to raise_error(TypeError) { |e| expect(e.message).to eq(msg) }
    end

    it 'lanza excepción si no recibe un objeto IO como pipe de escritura' do
      read, write = IO.pipe
      write = 'Cosa rara'
      msg = 'Error, se esperaba un Pipe'
      expect { Cliente.new(read, write) }.to raise_error(TypeError) { |e| expect(e.message).to eq(msg) }
    end

    it 'lanza una excepción si recibe como primer parámetro un pipe de escritura' do
      _, write = IO.pipe
      msg = 'Error, se esperaba un pipe de lectura'
      expect { Cliente.new(write, write) }.to raise_error(TypeError) { |e| expect(e.message).to eq(msg) }
    end

    it 'lanza una excepción si recibe como segundo parámetro un pipe de lectura' do
      read, = IO.pipe
      msg = 'Error, se esperaba un pipe de escritura'
      expect { Cliente.new(read, read) }.to raise_error(TypeError) { |e| expect(e.message).to eq(msg) }
    end
  end
end

describe 'pedir()' do
  it 'escribe en el pipe de escritura la ruta del fichero' do
    comprobar_que_cliente_pide_ruta('/mnt/test/file')
  end

  it 'escribe en el pipe de escritura la ruta solicitada' do
    comprobar_que_cliente_pide_ruta('/home/pepe/otra_ruta.rb')
  end

  it 'lee datos de la tubería hasta recibir EOF' do
    respuestas = ['Primer Valor', 'Segundo Valor']
    comprobar_resultado_de_pedir(respuestas)
  end

  it 'devuelve los datos que lee de la tubería' do
    respuestas = ['Algo diferente']
    comprobar_resultado_de_pedir(respuestas)
  end
end

def comprobar_que_cliente_pide_ruta(ruta)
  read, write = IO.pipe
  cliente = Cliente.new(read, write)

  write_double = instance_double('IO', puts: nil)
  read_spy = spy('IO')
  cliente.instance_variable_set(:@write, write_double)
  cliente.instance_variable_set(:@read, read_spy)

  cliente.pedir(ruta)
  expect(write_double).to have_received(:puts).with(ruta)
end

def comprobar_resultado_de_pedir(respuestas)
  read, write = IO.pipe
  cliente = Cliente.new(read, write)

  read_double = mock_read_pipe(respuestas)
  cliente.instance_variable_set(:@read, read_double)

  respuesta_recibida = cliente.pedir('test/path')
  expect(respuesta_recibida).to eq(respuestas.join)
end

def mock_read_pipe(respuestas)
  read_double = instance_double('IO')
  allow(read_double).to receive(:gets).and_return(*respuestas)

  eof_array = Array.new(respuestas.length, false) << true
  allow(read_double).to receive(:eof?).and_return(*eof_array)

  read_double
end
