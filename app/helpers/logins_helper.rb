module LoginsHelper
  def is_admin?
    user = User.find_by(id: session[:user_id])
    unless session[:user_id] && user.admin?
      redirect_to login_path
    end
  end

  def logged_in?
    unless session[:user_id]

    end
  end

  def current_user
    User.find_by(id: session[:user_id])
  end 
end
