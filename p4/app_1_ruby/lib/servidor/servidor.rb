require 'socket'

class Server
  def initialize(server_address)
    @server_address = server_address
  end

  def run
    start_server
    answer_requests
  end

  def stop
    @socket.close
    File.unlink(@server_address)
  end

  private

  def start_server
    socket_address = Addrinfo.unix(@server_address)

    @socket = Socket.new(Socket::PF_LOCAL, Socket::SOCK_STREAM)
    @socket.bind(socket_address)
    @socket.listen(1)
  rescue SystemCallError
    puts "Error: el socket #{socket_address} ya está en uso"
    exit
  end

  def answer_requests
    loop do
      ns, _ = @socket.accept
      fork do
        worker = Worker.new(ns) 
        worker.run
      end
    end
  end
end

class Worker
  @@MaxBytes = 100

  def initialize(socket)
    @socket = socket
  end

  def run
    path = read_path
    send_file(path)
  end

  private

  def read_path
    path = ''
    loop do
      received_fragment = @socket.recv(@@MaxBytes) 
      path += received_fragment

      break if received_fragment.size < @@MaxBytes
    end
    path
  end

  def send_file(path)
    begin
      IO.readlines(path).each { |line| @socket.send(line, 0) }
    rescue SystemCallError, IOError
      @socket.send("Error: no se pudo leer el fichero '#{path}'", 0)
    ensure
      @socket.shutdown(Socket::SHUT_RDWR)
    end
  end
end

