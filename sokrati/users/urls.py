from django.urls import path
from . import views as UserView
from django.contrib.auth import views as authViews


urlpatterns = [
    path('', UserView.homePage, name='home'),
    path('reg/', UserView.register, name='register'),
    path('profile/', UserView.profile, name='profile'),
    path('user/', authViews.LoginView.as_view(template_name='users/user.html'), name='user'),
    path('exit/', authViews.LogoutView.as_view(template_name='users/exit.html'), name='exit'),
    path('about/', UserView.about, name='about'),

]