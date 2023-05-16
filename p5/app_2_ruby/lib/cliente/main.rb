require_relative 'client'

Process.setproctitle('cli5')

print 'Introduzca la dirección del servidor: '
server_address = gets.chomp

print 'Introduzca el puerto del servidor: '
server_port = gets.chomp

client = Client.new(server_address, server_port)
client.request

