class PagesController < ApplicationController

  include LoginsHelper
  include UsersHelper

  def home
  end

  def software
  end

  def hardware
  end

  def prep
  end

  def admin
    is_admin?
  end
end
