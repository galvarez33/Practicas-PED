require 'singleton'

class Gatekeeper
  include Singleton

  def initialize
    @logged_users = Set.new
  end

  def validate(user)
    raise UserValidationError, 'User already logged' unless @logged_users.add?(user)
  end
end

class UserValidationError < StandardError
end
