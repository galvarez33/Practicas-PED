require 'socket'

class Client
  @@MaxBytes = 100

  def initialize(server_address)
    @server_address = server_address
    @socket = Socket.new(Socket::PF_LOCAL, Socket::SOCK_STREAM)
  end

  def request(path)
    open_conection(path)
    read_answer
    close_connection
  end

  private

  def open_conection(path)
    socket_address = Addrinfo.unix(@server_address)
    @socket.connect(socket_address)
    @socket.send(path, 0)
  rescue SystemCallError
    sleep(0.1)
    retry
  end

  def read_answer
    loop do
      message = @socket.recv(@@MaxBytes)
      break if message.empty?
      
      print message
    end
    puts
  end

  def close_connection 
    @socket.shutdown(Socket::SHUT_RDWR)
  end
end

