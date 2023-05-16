require_relative 'cliente'
require_relative 'servidor'

read_cliente, write_servidor = IO.pipe
read_servidor, write_cliente = IO.pipe

fork do
  Process.setproctitle('serv2')
  write_cliente.close

  servidor = Servidor.new(read_servidor, write_servidor)
  servidor.atender
end

# Código para el cliente

Process.setproctitle('cli2')
write_servidor.close

cliente = Cliente.new(read_cliente, write_cliente)
respuesta = cliente.pedir(ENV['FICHERO_CLIENTE'])
puts respuesta

Process.wait
