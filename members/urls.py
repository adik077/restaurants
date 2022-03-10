from django.urls import path
from django.contrib.auth import views as auth_views
from .views import Register, UpdateUserInfo, ChangePassword, change_password_done,login_user,logout_user

urlpatterns = [
    #path('login/',auth_views.LoginView.as_view(), name='login'),
    path('login/',login_user, name='login'),
    path('logout/',logout_user, name='logout'),
    path('register/',Register.as_view(), name='register'),
    path('update_profile/',UpdateUserInfo.as_view(), name='update_profile'),
    path('password/',ChangePassword.as_view(), name='change_password'),
    path('change_password_done/',change_password_done, name='change_password_done'),
]