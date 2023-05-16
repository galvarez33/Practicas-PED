class Servidor
  def initialize(ruta_fifo)
    @fifo = abrir_fifo(ruta_fifo)
  end

  def arrancar
    loop do
      id_cliente = @fifo.gets
      responder(id_cliente.chomp) if id_cliente
    end
  rescue Interrupt
    puts "\nApagando servidor..."
    @fifo.close
  end

  private

  def abrir_fifo(ruta_fifo)
    File.mkfifo(ruta_fifo) unless File.exist? ruta_fifo
    File.open(ruta_fifo, mode: 'r')
  rescue IOError
    puts "Error: no se pudo abrir la FIFO: '#{ruta_fifo}'"
  end

  def responder(id_cliente)
    ruta_fifo = "/tmp/#{id_cliente}_ped6_rb"
    File.mkfifo(ruta_fifo)

    File.open(ruta_fifo, 'w') do |fifo|
      date = Time.now
      fifo.puts date
    end

    File.delete(ruta_fifo)
  rescue SystemCallError
    puts "Error: no se pudo responder al cliente: '#{id_cliente}'"
    raise
  end
end
