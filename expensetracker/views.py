from django.shortcuts import render, redirect

def landing(request):
    print("CURRENT USER HAS ID: ",request.user.id)
    return render(request,'landing.html')

