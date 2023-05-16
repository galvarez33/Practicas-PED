require 'servidor'

describe Servidor do
  it 'es subclase de Agente' do
    expect(Servidor.superclass).to be(Agente)
  end

  describe 'initialize' do
    it 'guarda el pipe de lectura recibido' do
      read, write = IO.pipe
      servidor = Servidor.new(read, write)
      expect(servidor.instance_variable_get(:@read)).to be(read)
    end

    it 'guarda el pipe de escritura recibido' do
      read, write = IO.pipe
      servidor = Servidor.new(read, write)
      expect(servidor.instance_variable_get(:@write)).to be(write)
    end

    it 'lanza excepción si no recibe un objeto IO como pipe de lectura' do
      read, write = IO.pipe
      read = 'Jaja'
      msg = 'Error, se esperaba un Pipe'
      expect { Servidor.new(read, write) }.to raise_error(TypeError) { |e| expect(e.message).to eq(msg) }
    end
  end

  describe 'atender' do
    it 'abre el fichero recibido por el pipe de lectura' do
      ruta = '/dev/null'
      comprobar_que_servidor_abre_el_fichero_adecuado(ruta)
    end

    it 'abre el fichero recibido por el pipe de lectura' do
      ruta = '/otra/ruta'
      comprobar_que_servidor_abre_el_fichero_adecuado(ruta)
    end

    it 'escribe en el pipe las líneas del fichero' do
      contenido = ['First line', 'Second line']
      write_double = preparar_escenario_respuesta(contenido)

      expect(write_double).to have_received(:puts).with(contenido[0])
    end

    it 'escribe en el pipe las líneas leídas del fichero' do
      contenido = ['Different first line', 'Second line']
      write_double = preparar_escenario_respuesta(contenido)

      expect(write_double).to have_received(:puts).with(contenido[0])
    end

    it 'realmente escribe todas las líneas del fichero' do
      contenido = ['Different first line', 'Second line']
      write_double = preparar_escenario_respuesta(contenido)

      expect(write_double).to have_received(:puts).with(contenido[1])
    end

    it 'devuelve error si no se puede abrir el fichero' do
      ruta = '/test/file'
      servidor = crear_servidor(ruta)

      write_double = instance_double('IO', puts: nil)
      allow(write_double).to receive(:close)
      servidor.instance_variable_set(:@write, write_double)

      allow(IO).to receive(:readlines).and_raise(Errno::ENOENT)
      servidor.atender

      error_msg = "Error: no se pudo leer el fichero '#{ruta}'"
      expect(write_double).to have_received(:puts).with(error_msg)
    end

    it 'indica la ruta del fichero que causó el error' do
      ruta = '/another/file'
      servidor = crear_servidor(ruta)

      write_double = instance_double('IO', puts: nil)
      allow(write_double).to receive(:close)
      servidor.instance_variable_set(:@write, write_double)

      allow(IO).to receive(:readlines).and_raise(Errno::ENOENT)
      servidor.atender

      error_msg = "Error: no se pudo leer el fichero '#{ruta}'"
      expect(write_double).to have_received(:puts).with(error_msg)
    end

    it 'cierra el pipe una vez escrito el fichero' do
      write_double = preparar_escenario_respuesta([])
      expect(write_double).to have_received(:close)
    end

    it 'cierra el pipe una vez escrito el mensaje de error' do
      servidor = crear_servidor('/dev/null')

      write_double = instance_double('IO', puts: nil)
      allow(write_double).to receive(:close)
      servidor.instance_variable_set(:@write, write_double)

      allow(IO).to receive(:readlines).and_raise(Errno::ENOENT)
      servidor.atender

      expect(write_double).to have_received(:close)
    end

    it 'limpia el \n del final de la ruta' do
      ruta = "/dev/null\n"
      servidor = crear_servidor(ruta)

      allow(IO).to receive(:readlines).and_return([])
      servidor.atender
      expect(IO).to have_received(:readlines).with(ruta.chomp)
    end
  end
end

def comprobar_que_servidor_abre_el_fichero_adecuado(ruta)
  servidor = crear_servidor(ruta)

  content = []
  allow(IO).to receive(:readlines).and_return(content)

  servidor.atender
  expect(IO).to have_received(:readlines).with(ruta)
end

def preparar_escenario_respuesta(contenido)
  servidor = crear_servidor('/dev/null')

  write_double = instance_double('IO', puts: nil)
  allow(write_double).to receive(:close)
  servidor.instance_variable_set(:@write, write_double)

  allow(IO).to receive(:readlines).and_return(contenido)

  servidor.atender

  write_double
end

def crear_servidor(ruta)
  read, write = IO.pipe
  servidor = Servidor.new(read, write)

  read_double = instance_double('IO', gets: ruta)
  servidor.instance_variable_set(:@read, read_double)

  servidor
end

class MockFile
  def initialize(lines)
    @lines = lines
  end
end
