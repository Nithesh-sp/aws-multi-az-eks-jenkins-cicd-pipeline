# urls.py

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from business.views import home_page

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('signin/', views.signin_view, name='signin'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    # Add other URLs as needed
]
