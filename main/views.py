from django.shortcuts import render, redirect



def home(request):
    return render(request, 'main/home.html')



def login_view(request):
    return render(request, 'main/login.html')



def logout_view(request):
    return redirect("home_page")