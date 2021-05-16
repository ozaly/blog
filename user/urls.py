from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from Article  import views
from . import views

app_name="user"
urlpatterns = [
    path('register/', views.register,name="register"),
    path('login/', views.loginUser,name="login"),
    path('logout/', views.logoutUser,name="logout"),



]