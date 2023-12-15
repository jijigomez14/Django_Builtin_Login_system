# home/urls.py
from django.urls import path

from . import views  # Corrected import statement
from .views import login_view
urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/', login_view, name='registration/login'), 
    path('logout/', views.logout_view, name='logout'), # Added the view parameter
]
