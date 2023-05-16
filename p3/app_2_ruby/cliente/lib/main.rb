require_relative 'cliente'

Process.setproctitle('cli3')

fifo_servidor = ENV['RUTA_FIFO'] || '/tmp/app_2_fifo_ped6_rb'
pid = Process.pid

cliente = Cliente.new(pid, fifo_servidor)
cliente.pedir
