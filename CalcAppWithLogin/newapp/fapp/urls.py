from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('calculator', views.calculator, name='calculator'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('about', views.about, name='about'),
]
