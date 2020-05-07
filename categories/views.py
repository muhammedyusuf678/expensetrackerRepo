from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required

# Create your views here.

from .models import Category

from datetime import datetime

@login_required(login_url="/accounts/login")
def allCategories (request):
    allCategoriesForUser = Category.objects.filter(user=request.user)
    defaultCategories = Category.objects.filter(user=1) #set by admin user

    return render(request,"categories/allCategories.html",{'categories':allCategoriesForUser, 'defaultCategories':defaultCategories })

@login_required(login_url="/accounts/login")
def addCategory (request):
    if request.method == 'POST':
        if request.POST['value']:
            newCategory = Category()
            newCategory.value = request.POST['value']
            newCategory.user = request.user
            newCategory.save()
            return redirect('allCategories')
    else: 
        return render(request,'categories/addCategory.html')

def editCategory (request, category_id):
    categoryToEdit = Category.objects.get(pk=category_id)
    if request.method == 'POST':
        if request.POST['value']:
            categoryToEdit.value = request.POST['value']
            categoryToEdit.save()
            return redirect('allCategories')
    else: 
        return render(request,'categories/editCategory.html',{'category':categoryToEdit})

def deleteCategory (request, category_id):
    Category.objects.get(pk=category_id).delete()
    return redirect('allCategories')

