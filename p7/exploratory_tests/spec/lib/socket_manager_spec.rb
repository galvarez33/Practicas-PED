require 'socket_manager'
require 'socket'

describe SocketManager do
  it 'is singleton' do
    expect(SocketManager).to include(Singleton)
  end

  describe 'register' do
    it 'adds a user-socket map' do
      socket_manager = SocketManager.instance

      user = User.new('tommy')
      socket = Socket.new(Socket::PF_INET, Socket::SOCK_STREAM)

      socket_manager.register(user, socket)
      expect(socket_manager.socket_map[user]).to eq(socket)
    end
  end
end
