class Agente
  def initialize(read, write)
    @read = read
    @write = write

    validar_pipe(@read, 'lectura') { @read.puts 'test' }
    validar_pipe(@write, 'escritura') { @write.read_nonblock(0) }
  end

  private

  def validar_pipe(pipe, message)
    raise TypeError, 'Error, se esperaba un Pipe' unless pipe.is_a? IO

    begin
      yield
      raise TypeError, "Error, se esperaba un pipe de #{message}"
    rescue IOError
    end
  end
end
