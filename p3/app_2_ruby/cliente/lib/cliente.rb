class Cliente
  def initialize(id, fifo_servidor)
    @id = id
    @fifo_servidor = fifo_servidor
  end

  def pedir
    raise SystemCallError, nil unless File.exist? @fifo_servidor

    File.open(@fifo_servidor, mode: 'w') do |write_fifo|
      write_fifo.puts @id
    end
    leer_respuesta
  rescue SystemCallError
    puts "Error: No se pudo abrir la FIFO '#{@fifo_servidor}'"
  end

  private

  def leer_respuesta
    File.open("/tmp/#{@id}_ped6_rb", mode: 'r') do |read_fifo|
      puts read_fifo.gets
    end
  rescue SystemCallError
    sleep 0.1
    retry
  end
end
