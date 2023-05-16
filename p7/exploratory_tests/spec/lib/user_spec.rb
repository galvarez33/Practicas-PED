require 'user'

describe User do
  it 'has username' do
    username = 'tommy'
    user = User.new(username)
    expect(user.name).to eq(username)
  end

  it 'stores provided username' do
    username = 'rosa'
    user = User.new(username)
    expect(user.name).to eq(username)
  end
end
