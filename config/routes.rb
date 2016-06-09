Rails.application.routes.draw do
  root 'pages#home'
  get 'about', to: 'pages#about'
  get 'prep', to: 'pages#prep'
  get 'hardware', to: 'pages#hardware'
  get 'software', to: 'pages#software'
  get 'process', to: 'pages#process'

  # Don't mind the routes below
  get 'admin', to: 'pages#admin'

  get 'login', to: "logins#new"
  post 'login', to: 'logins#create'
  delete 'logout', to: 'logins#destroy'
end
