from django.urls import path, include
from users.views import Register
from . import views


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('home', views.home, name='home'),
    path('register/', Register.as_view(), name='register'),
    path('about', views.about, name='about'),
]