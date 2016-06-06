module LoginsHelper
  def is_admin?(user)
    unless user.admin?
      redirect_to root_path
    end
  end
end
