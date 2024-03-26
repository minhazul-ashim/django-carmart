from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('login/', views.LoginPageView.as_view(), name="loginPage"),
    path('register/', views.RegisterView.as_view(), name="registerPage"),
    path('profile/', login_required(views.ProfileView), name="profilePage"),
    path('logout/', views.userlogout, name="logout"),
]
