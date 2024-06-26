from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='common/login.html'), name="login"), #로그인
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), #로그아웃
    path('signup/', views.signup, name="signup"),  #회원가입
]