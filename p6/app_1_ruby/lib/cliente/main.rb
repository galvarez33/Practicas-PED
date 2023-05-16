require_relative 'client'

Process.setproctitle('cli6')

$stderr.print 'Introduzca la dirección del servidor: '
server_address = gets.chomp

$stderr.print 'Introduzca el puerto del servidor: '
server_port = gets.chomp

$stderr.print 'Introduzca la ruta del fichero: '
path = gets.chomp

client = Client.new(server_address, server_port)
client.request(path)

