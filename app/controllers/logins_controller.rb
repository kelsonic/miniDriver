class LoginsController < ApplicationController

  def new
  end

  def create
    @user = User.find_by(email: session_params[:email])
    if @user && @user.authenticate(session_params[:password])
      session[:user_id] = @user.id
      flash[:success] = "Welcome #{@user.username}. You are now logged in."
      redirect_to root_path
    else
      flash[:errors] = ["Email or password was incorrect."]
      render 'new'
    end
  end

  def destroy
    session[:user_id] = nil
    flash[:success] = "You logged out successfully."
    redirect_to root_path
  end

  private
    def session_params
      params.require(:session).permit(:email, :password)
    end

end
