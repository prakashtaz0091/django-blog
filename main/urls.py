from django.urls import path
from .import views

urlpatterns = [

    # auth
    path('accounts/login/', views.login_view, name="login_page"),
    path('accounts/logout/', views.logout_view, name="logout_page"),


    
    path('', views.home, name="home_page"),
]