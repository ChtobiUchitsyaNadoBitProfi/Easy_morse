from django.urls import path, include
from users.views import Register
from . import views


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('home', views.home, name='home'),
    path('clickboard', views.clickboard, name='clickboard'),
    path('radiogram', views.radiogram, name='radiogram'),
    path('register/', Register.as_view(), name='register'),
    path('about', views.about, name='about'),

]