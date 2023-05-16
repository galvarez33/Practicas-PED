require 'singleton'

class SocketManager
  include Singleton

  attr_reader :socket_map

  def initialize
    @socket_map = {}
  end

  def register(user, socket)
    @socket_map[user] = socket
  end
end
