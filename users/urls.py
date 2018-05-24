from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.signup, name='signup_url'),
    path('logout/', views.logout_view, name='logout_url'),
    path('login/', views.login_view, name='login_url'),
]
