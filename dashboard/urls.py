from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register_user,name='register-user'),
    path('login',views.login_user,name='login-user'),
    path('dashboard',views.user_dashboard,name='profile'),
    
    path('questions',views.view_questions,name='all-questions'),
    path('logout',views.logout_user,name='logout-user'),
]