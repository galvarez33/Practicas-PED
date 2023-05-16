require_relative 'client'

Process.setproctitle('cli4')

print 'Introduzca la dirección del servidor: '
server_address = gets.chomp

print 'Introduzca la ruta del fichero: '
path = gets.chomp

client = Client.new(server_address)
client.request(path)

