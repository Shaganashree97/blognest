from django.shortcuts import render, redirect, HttpResponse
from .models import BlogPost
from .forms import BlogPostForm

from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm

# Create your views here.
def base(request):
    return HttpResponse("Hello World")

def bloglist(request):
    if not request.user.is_authenticated:
        messages.info(request, "Please log in to access the home page.")
        return redirect(f'/login/?next={request.path}')
    
    blogs = BlogPost.objects.all
    return render(request, 'bloglist.html', {'blogs':blogs})

def create_blog(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(bloglist)
    else:
        form=BlogPostForm()
    return render(request, 'create_blog.html', {'form':form})

def register_view(request):
    if request.user.is_authenticated:
        return redirect('blog')

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Welcome {user.username}, your account has been created!")
            return redirect('blog')  
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('blog')

    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():  
            username = form.cleaned_data.get('username') 
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back {user.username}!")
                return redirect('blog')  
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = UserLoginForm()
    storage = messages.get_messages(request)
    storage.used = True

    return render(request, 'login.html', {'form': form})

def logout_view(request):
    storage = messages.get_messages(request)
    storage.used = True
    username = request.user.username

    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('login')

