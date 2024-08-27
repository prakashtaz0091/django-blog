from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .models import Profile, Post
from .forms import CreateBlogForm, CategoryForm




# def blog_detail(request, blog_id):

def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home_page")
        else:
            return render(request, "main/add_category.html", {'form':form})
    else:
        form = CategoryForm()
        return render(request, "main/add_category.html", {'form':form})


def create_post(request):

    if request.method == "POST":
        form = CreateBlogForm(request.POST)

        if form.is_valid():
            form.save(author = request.user)

            return redirect("home_page")
        else:
            return render(request, "main/create_blog.html", {'form':form})


    form = CreateBlogForm()


    return render(request, 'main/create_blog.html', {'form':form})


def home(request):

    latest_blogs = Post.objects.all().order_by('-created_at')

    context = {
        'blogs':latest_blogs
    }


    return render(request, 'main/home.html', context)



def signup_view(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
      

        try:
            user = User.objects.get(username=username)
            return render(request, 'main/signup.html', {'error':"Username must be unique"})
        except User.DoesNotExist:
                
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

                user = User.objects.create_user(username, password=password, first_name=first_name, last_name=last_name)

                if profile_pic:
                    # print(profile_pic, "*******************")
                    Profile.objects.create(profile_pic=profile_pic, user=user)
                



                return redirect('login_page')

   


    return render(request, 'main/signup.html')

def login_view(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')
        # print(remember_me,"****************")

        # print(username, password)

        try:
            user = authenticate(request, username=username, password=password)
        except User.DoesNotExist:
            return render(request, 'main/login.html', {'error':'Invalid Credentials'})
        else:
            if user is None:
                return render(request, 'main/login.html', {'error':'Invalid Credentials'})

            login(request, user)
            if remember_me:
                request.session.set_expiry(7*24*60*60)

            return redirect("home_page")




    return render(request, 'main/login.html')



def logout_view(request):

    logout(request)

    return redirect("home_page")