from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="login_page")
def index(request):
    return render(request,"index.html")

def login_view(request):
    if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = User.objects.filter(username = username)
            if not user.exists():
                messages.success(request,"user not found")
                return redirect('/login/')
            user = authenticate(username = username , password = password)
            print(user)
            if not user:
                messages.success(request , "Incorrect password")

                return redirect('/login/')
            login(request , user)
            return redirect('/')

    return render(request,"login.html" )



def logout_view(request):
    logout(request)
    return redirect('/login/')



def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')


        user = User.objects.filter(username = username)
        if user.exists():
           messages.success(request,"username already taken")
           return redirect('/register/')
        
        user = User.objects.create(
            username = username,
            first_name = first_name,
            last_name = last_name
        )
        user.set_password(password)
        user.save()
        messages.success(request,"Account Created")
        return redirect('/register/')

        




    return render(request,"register.html" )

