from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required

# Create your views here.

# from .models import Category

from datetime import datetime

@login_required(login_url="/accounts/login")
def allPaymentMethods (request):
    
    return render(request,"categories/allCategories.html")



