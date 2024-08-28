from django.urls import path
from .import views

urlpatterns = [

    # auth
    path('accounts/signup/', views.signup_view, name="signup_page"),
    path('accounts/login/', views.login_view, name="login_page"),
    path('accounts/logout/', views.logout_view, name="logout_page"),


    
    path('', views.home, name="home_page"),
    path('blog/create/', views.create_post, name="create_post_page"),
    path('blog/<int:blog_id>/', views.blog_detail, name="blog_detail_page"),
    path('blog/category/add/', views.add_category, name="add_category_page"),
    path('comment/', views.add_comment, name="add_comment"),
    path('blog/like/<int:blog_id>/', views.add_like, name="add_like"),


]