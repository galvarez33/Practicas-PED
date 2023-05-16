require_relative 'agente'

class Servidor < Agente
  def atender
    ruta = @read.gets.chomp

    begin
      IO.readlines(ruta).each { |line| @write.puts line }
    rescue SystemCallError
      @write.puts "Error: no se pudo leer el fichero '#{ruta}'"
    ensure
      @write.close
    end
  end
end
