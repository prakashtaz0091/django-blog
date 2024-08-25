from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth.models import User

def home(request):
    return render(request, 'main/home.html')



def signup_view(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        # # signup_form = UserCreationForm(username=username, password1=password, password2 = password_confirm)
        # signup_form = UserCreationForm(request.POST)

        # if signup_form.is_valid():
        #     print("valid")
        if len(username) <6 and '@' not in username:
            return render(request, 'main/signup.html', {'error':"Username must be at least 6 chars long or it must contain @"})
        elif password != password_confirm:
            return render(request, 'main/signup.html', {'error':"Password  and Confirm Password must be same "})
        elif len(password) <6 and len(password_confirm) <6:
            return render(request, 'main/signup.html', {'error':"Password  must be at least 6 chars long "})
        else:

            first_name = request.POST.get('first_name', 'default_name')
            last_name = request.POST.get('last_name', 'default_name')
            profile_pic = request.FILES.get('profile_picture')

            user = User(
                username = username  
            )
            user.password = user.set_password(password)
            user.first_name = first_name
            user.last_name = last_name

            if profile_pic:
                print(profile_pic, "*******************")



            return redirect('login_page')

   


    return render(request, 'main/signup.html')

def login_view(request):
    return render(request, 'main/login.html')



def logout_view(request):
    return redirect("home_page")