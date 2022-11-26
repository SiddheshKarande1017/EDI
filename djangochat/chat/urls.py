from django.urls import path
from . import views

urlpatterns=[
    path('',views.register, name='register'),
    path('login/', views.loginuser, name="login"),
    path('login/home', views.home, name='home'),

]