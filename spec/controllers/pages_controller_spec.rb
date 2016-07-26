require 'rails_helper'

RSpec.describe PagesController, type: :controller do
  describe 'GET #home' do
    
    before {
      get :home
    }

    it { should respond_with(200) }

    it { should route(:get, '/').to(action: :home) }
    
    it { should render_template('home') }
  end

  describe 'GET #software' do
    
    before {
      get :software
    }

    it { should respond_with(200) }

    it { should route(:get, '/software').to(action: :software) }
    
    it { should render_template('software') }
  end

  describe 'GET #hardware' do
    
    before {
      get :hardware
    }

    it { should respond_with(200) }

    it { should route(:get, '/hardware').to(action: :hardware) }
    
    it { should render_template('hardware') }
  end

  describe 'GET #prep' do
    
    before {
      get :prep
    }

    it { should respond_with(200) }

    it { should route(:get, '/prep').to(action: :prep) }
    
    it { should render_template('prep') }
  end

  describe 'GET #about' do
    
    before {
      get :about
    }

    it { should respond_with(200) }

    it { should route(:get, '/about').to(action: :about) }
    
    it { should render_template('about') }
  end
end