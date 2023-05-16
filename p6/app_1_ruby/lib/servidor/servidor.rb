require 'socket'

class Server
  def initialize(port)
    @port = port
  end

  def run
    start_server
    answer_requests
  end

  def stop
    @socket.shutdown(Socket::SHUT_RDWR)
  end

  private

  def start_server
    @socket = TCPServer.new('0.0.0.0', @port)
    @socket.listen(1)
  rescue SystemCallError
    puts "Error: el puerto #{@port} ya está en uso"
    exit
  end

  def answer_requests
    loop do
      ns = @socket.accept
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
      File.open(path) do |file|
        until file.eof? do
          data = file.read(@@MaxBytes)
          @socket.send(data, 0)
        end
      end
    rescue SystemCallError, IOError
      @socket.send("Error: no se pudo leer el fichero '#{path}'", 0)
    ensure
      @socket.shutdown(Socket::SHUT_RDWR)
    end
  end
end

