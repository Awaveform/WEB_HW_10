from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('sign_up/', views.sign_up_user, name='sign_up'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
]
