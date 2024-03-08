from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

def home(request):
    return render(request,'Dashboard.html')
def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('paas1')
        password2 = request.POST.get('paas2')
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = firstname
        myuser.last_name = lastname

        myuser.save()

        messages.success(request,"Your account has been successfully created")

        return redirect('signin')
    return render(request,'signup.html')
def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('pass1')

        User = authenticate(request,username=username,password=password)

        if User is not None:
            login(request, User)
            fname = User.first_name
            return render(request, 'index.html', {'fname':fname})
        else:
            messages.error(request, "Bad credentials")
            return redirect('Dashboard')
    return render(request,'signin.html')
def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('Dashboard')

# Create your views here.
