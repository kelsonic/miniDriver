Rails.application.routes.draw do
  root 'pages#home'
  get 'hardware', to: 'pages#hardware'
  get 'code', to: 'pages#code'
  get 'machine-learning', to: 'pages#machine_learning'
  get 'admin', to: 'pages#admin'

  get 'login', to: "logins#new"
  post 'login', to: 'logins#create'
  delete 'logout', to: 'logins#destroy'
end
