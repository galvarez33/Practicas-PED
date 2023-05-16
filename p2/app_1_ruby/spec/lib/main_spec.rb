require 'cliente'
require 'agente'

describe 'main script' do
  before :each do
    mock_pipes
    mock_cliente
    mock_servidor

    # Silencia los puts del cliente
    allow_any_instance_of(Object).to receive(:puts)
    allow(Process).to receive(:wait)
  end

  it 'hace fork para crear dos procesos' do
    expect_any_instance_of(Object).to receive(:fork)
    load('main.rb')
  end

  describe 'cliente' do
    it 'recibe los pipes de lectura y escritura adecuados' do
      load('main.rb')

      expect(Cliente).to have_received(:new).with(@read_cliente, @write_cliente)
    end

    it 'cambia el nombre del proceso a "cli2"' do
      allow(Process).to receive(:setproctitle)

      load('main.rb')

      expect(Process).to have_received(:setproctitle).with('cli2')
    end

    it 'muestra por la salida estándar el resultado de pedir un fichero' do
      respuesta = 'test'
      comprobar_salida_estandar(respuesta)
    end

    it 'muestra por la salida estándar el resultado de pedir un fichero' do
      respuesta = 'otra respuesta'
      comprobar_salida_estandar(respuesta)
    end

    it 'pide el fichero configurado en la variable de entorno FICHERO_CLIENTE' do
      comprobar_ruta_cliente('/test/path')
    end

    it 'realmente pide el fichero configurado en la variable de entorno FICHERO_CLIENTE' do
      comprobar_ruta_cliente('/another/path')
    end

    it 'espera a que finalice el servidor antes de cerrar el programa' do
      expect(Process).to receive(:wait)
      load('main.rb')
    end

    it 'cierra el pipe de escritura del servidor (no va a ser usado por el cliente)' do
      expect(@write_servidor).to receive(:close)
      load('main.rb')
    end
  end

  describe 'servidor' do
    it 'recibe los pipes de lectura y escritura adecuados' do
      load('main.rb')
      expect(Servidor).to have_received(:new).with(@read_servidor, @write_servidor)
    end

    it 'cambia el nombre del proceso a "serv2"' do
      allow(Process).to receive(:setproctitle)

      load('main.rb')

      expect(Process).to have_received(:setproctitle).with('serv2')
    end

    it 'lanza el servidor' do
      expect(@servidor_double).to receive(:atender)
      load('main.rb')
    end

    it 'cierra el pipe de escritura del cliente (no va a ser usado por el servidor)' do
      expect(@write_cliente).to receive(:close)
      load('main.rb')
    end
  end
end

def mock_pipes
  @read_cliente, @write_servidor = IO.pipe
  @read_servidor, @write_cliente = IO.pipe

  allow(IO).to receive(:pipe).and_return(
    [@read_cliente, @write_servidor], [@read_servidor, @write_cliente]
  )
end

def mock_cliente
  @cliente_double = instance_double('Cliente', pedir: 'test')
  allow(Cliente).to receive(:new).and_return(@cliente_double)
end

def mock_servidor
  @servidor_double = instance_double('Servidor', atender: nil)
  allow(Servidor).to receive(:new).and_return(@servidor_double)
  allow_any_instance_of(Object).to receive(:fork).and_yield
end

def comprobar_salida_estandar(respuesta)
  allow(@cliente_double).to receive(:pedir).and_return(respuesta)

  expect_any_instance_of(Object).to receive(:puts).with(respuesta)

  load('main.rb')
end

def comprobar_ruta_cliente(ruta)
  ENV['FICHERO_CLIENTE'] = ruta
  expect(@cliente_double).to receive(:pedir).with(ruta)

  load('main.rb')
end
