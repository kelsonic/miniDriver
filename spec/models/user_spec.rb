require 'rails_helper'

RSpec.describe User, type: :model do
  
  describe 'its username' do
    it { should validate_presence_of(:username) }
    it { should validate_length_of(:username).is_at_least(3) }
    it { should validate_length_of(:username).is_at_most(75) }
  end

  describe 'its password' do
    it { should have_secure_password }
  end

end