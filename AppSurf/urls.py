from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('',inicio,name="Inicio"),
    path('login/',loginview, name="Login"),
    path('registro/',register, name="Registrar"),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name="Logout"),
]