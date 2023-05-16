require 'gatekeeper'
require 'user'

describe Gatekeeper do
  it 'is singleton' do
    expect(Gatekeeper).to include(Singleton)
  end

  describe 'validate' do
    it 'adds users to Set' do
      user = User.new('tommy')
      test_validation_stores_logged_user(user)
    end

    it 'really adds validated user to Set' do
      user = User.new('rosa')
      test_validation_stores_logged_user(user)
    end

    it 'raises error if user is added twice' do
      user = User.new('rosa')
      gatekeeper = Gatekeeper.instance

      gatekeeper.validate(user)
      expect { gatekeeper.validate(user) }.to raise_error(UserValidationError, 'User already logged')
    end
  end
end

def test_validation_stores_logged_user(user)
  gatekeeper = Gatekeeper.instance
  gatekeeper.validate(user)

  set = gatekeeper.instance_variable_get(:@logged_users)
  expect(set).to include(user)
end
