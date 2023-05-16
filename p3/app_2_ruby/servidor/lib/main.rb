require_relative 'servidor'

def redirect_std_fd(stdin, stdout, stderr)
  [$stdin, $stdout, $stderr].each(&:close)

  $stdin.reopen(stdin)
  $stdin.reopen(stdout)
  $stdin.reopen(stderr)
end

def start_server(ruta_fifo)
  servidor = Servidor.new(ruta_fifo)
  servidor.arrancar
end

ruta_fifo = ENV['RUTA_FIFO'] || '/tmp/app_2_fifo_ped6_rb'

# First fork -> lose terminal as parent
fork do
  # Decouple
  Process.setsid
  Dir.chdir('/')
  File.umask(0)

  # Second fork -> Don't be session leader to avoid future binding to ttys
  fork do
    Process.setproctitle('serv3')

    redirect_std_fd('/dev/null', '/dev/null', '/dev/null')
    start_server(ruta_fifo)
  end
end
