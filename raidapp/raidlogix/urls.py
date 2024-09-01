from django.urls import path
from . import views

urlpatterns = [
    path('', views.template, name="template"),
    path('home', views.home, name="home"),
    path('landing-page', views.login, name="landing-page")
]