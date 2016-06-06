module LoginsHelper
  def is_admin?
    user = User.find(session[:user_id])
    unless user.admin?
      redirect_to root_path
    end
  end
end
