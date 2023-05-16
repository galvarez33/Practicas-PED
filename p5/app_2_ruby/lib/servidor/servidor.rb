require 'socket'

class Server
  @@MaxBytes = 100

  def initialize(port)
    @port = port
  end

  def run
    start_server
    answer_requests
  end

  def stop
    @socket.close
  end

  private

  def start_server
    @socket = UDPSocket.new(Socket::AF_INET)
    @socket.bind('0.0.0.0', @port)
  rescue SystemCallError
    puts "Error: el puerto #{@port} ya está en uso"
    exit
  end

  def answer_requests
    loop do
      _, raw_address = @socket.recvfrom(@@MaxBytes, 0)
      date = Time.now
      client_address = Addrinfo.new(raw_address)
      @socket.sendmsg(date.to_s, 0, client_address)
    end
  end
end

