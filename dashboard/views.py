from django.shortcuts import render,redirect
from django.contrib import messages


# Django User Model for authentication 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    title='Welcome To Django-OverFlow | Home'
    return render(request,'home.html',{'title':title})

def register_user(request):
    title="Django-OverFlow | Register"
    if request.method=='POST':
        print("creating user")
        firstname=request.POST['firstname']
        username=request.POST['username']
        lastname=request.POST['lastname']
        email=request.POST['email']
        password=request.POST['password']
        if User.objects.filter(email=email).exists():
            messages.warning(request,'Email is Already taken Login Instead')
            return redirect('register-user')
        elif User.objects.filter(username=username).exists():
            messages.warning(request,'Username is Already taken try another')
            return redirect('register-user')
        user = User.objects.create_user(first_name=firstname,last_name=lastname,email=email,username=username,password=password)
        user.save()
        login(request,user)
        return redirect('home')
    return render(request,'auth/register.html',{'title':title})


def login_user(request):
    title="Django-OverFlow | Login"
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        if User.objects.filter(username=username).exists():
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.warning(request,'Invalid Credentials')
                return redirect('login-user')
        elif User.objects.filter(email=username).exists():
            username=User.objects.get(email=username).username
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('profile')
            else:
                messages.warning(request,'Invalid Credentials')
                return redirect('login-user')
        else:
            messages.warning(request,'User Not Found')
            return redirect('login-user')
    return render(request,'auth/login.html',{'title':title})

def user_dashboard(request):
    return render(request,'user/profile.html')

def view_questions(request):
    return render(request,'questions.html')


def logout_user(request):
    logout(request)
    return redirect('home')
