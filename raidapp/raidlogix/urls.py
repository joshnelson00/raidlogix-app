from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="login"),
    path('home', views.home, name="home"),
    path('landing-page', views.login, name="landing-page"),
    path('create-account', views.create_account, name="create_account"),
    path('sign-in', views.sign_in, name="sign_in"),
    path('projects', views.projects, name="projects"),
    path('sign-out', views.sign_out, name="sign_out"),
    path('create-project', views.create_project, name="create_project"),
    

]