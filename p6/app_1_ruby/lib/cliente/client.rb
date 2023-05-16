require 'socket'

class Client
  @@MaxBytes = 100

  def initialize(server_address, server_port)
    @server_address = server_address
    @server_port = server_port
  end

  def request(path)
    open_conection(path)
    read_answer
    close_connection
  end

  private

  def open_conection(path)
    @socket = TCPSocket.new(@server_address, @server_port)
    @socket.send(path, 0)
  rescue SystemCallError
    sleep(0.1)
    retry
  end

  def read_answer
    loop do
      message = @socket.recv(@@MaxBytes)
      break if message.empty?
      
      print message rescue print message.force_encoding('utf-8')
    end
  end

  def close_connection 
    @socket.shutdown(Socket::SHUT_RDWR)
  end
end

