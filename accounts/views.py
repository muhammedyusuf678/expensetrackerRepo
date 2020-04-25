from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            #check if there is existing user with username
            try:
                user = User.objects.get(username=request.POST['email'])
                return render (request,'accounts/signup.html',{'error':'There is already an account with this email'})
            except User.DoesNotExist:
                user = User.objects.create_user(username = request.POST['email'],password = request.POST['password1'], first_name =request.POST['fname'].capitalize(), last_name= request.POST['lname'].capitalize() )
     
                #login new user
                auth.login(request,user)
                return redirect('home')
        else:
            return render (request,'accounts/signup.html',{'error':'Passwords must match'})

    else:
        return render (request,'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username = request.POST['email'], password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else: 
            return render (request,'accounts/login.html', {'error':'Email or password is incorrect'})
    else: 
        return render (request,'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('landing')
   

