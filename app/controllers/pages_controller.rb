class PagesController < ApplicationController

  include LoginsHelper
  include UsersHelper

  def home
  end

  def code
  end

  def hardware
  end

  def machine_learning
  end

  def admin
    is_admin?(current_user)
  end
end
