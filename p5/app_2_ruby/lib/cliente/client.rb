require 'socket'

class Client
  @@MaxBytes = 100

  def initialize(server_address, server_port)
    @server_address = Addrinfo.udp(server_address, server_port)
    @socket = UDPSocket.new(Socket::AF_INET)
  end

  def request
    @socket.sendmsg('What time is it?', 0, @server_address)
    time, _ = @socket.recvfrom(@@MaxBytes, 0)
    puts time
    close_socket
  end

  private

  def close_socket
    @socket.close
  end
end

