require_relative 'servidor'

def redirect_std_fd(stdin, stdout, stderr)
  [$stdin, $stdout, $stderr].each(&:close)

  $stdin.reopen(stdin, 'r')
  $stdout.reopen(stdout, 'w+')
  $stderr.reopen(stderr, 'w+')
end

def start_server(server_address)
  server = Server.new(server_address)
  server.run
rescue SignalException => e
  server.stop
  exit
end

server_address = ENV['SERVER_PORT'] || '3333'

# First fork -> lose terminal as parent
fork do
  # Decouple
  Process.setsid
  Dir.chdir('/')
  File.umask(0)

  # Second fork -> Don't be session leader to avoid future binding to ttys
  fork do
    Process.setproctitle('serv5')

    redirect_std_fd('/dev/null', '/dev/null', '/dev/null')
    start_server(server_address)
  end
end

