class User < ActiveRecord::Base

  validates :username, presence: true, length: {in: 10..75}
  has_secure_password

end
