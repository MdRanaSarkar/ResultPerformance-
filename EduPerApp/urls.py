from django.urls import path
from .views import Home, Register, Login
urlpatterns = [
    path('', Home, name='home'),
    path('login/', Login, name='login'),
    path('register/', Register, name='register'),


]
