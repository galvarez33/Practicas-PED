require_relative 'agente'

class Cliente < Agente
  def pedir(ruta)
    @write.puts ruta
    respuesta = ''
    respuesta += @read.gets until @read.eof?
    respuesta
  end
end
