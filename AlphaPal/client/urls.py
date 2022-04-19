from django.urls import path
from .import views

urlpatterns = [
    path('', views.profile, name="profile"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
    path('user_profile_update/<str:pk>/', views.user_profile_update, name="user_profile_update"),
    ]