from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required

# Create your views here.
from expenses.models import Expense
from categories.models import Category
# import simplejson as json

from django.http import JsonResponse


@login_required(login_url="/accounts/login")
def statsIndex(request):
    #Entry.objects.filter(blog__name='Beatles Blog')
    # allCategoriesForUser = Category.objects.filter(user=request.user).all()
    yearOptions = list(range(2020,1970,-1))
    return render(request,'stats/statsIndex.html', {'years':yearOptions})

@login_required(login_url="/accounts/login")
def categoryAmountStat(request):
    print ("---------> in categoryAmountStat")
    print("from request yearAndMonth: ",request.GET["yearAndMonth"])
    yearAndMonthString = str(request.GET["yearAndMonth"])
    splittedYearAndMonth = yearAndMonthString.split("-")
    year = splittedYearAndMonth[0]
    month = splittedYearAndMonth[1]

    fromDateString = yearAndMonthString+"-01 00:00:00"
    toDateString = year+"-"+str(int(month)+1)+"-01 00:00:00"
    allExpensesForUser = Expense.objects.filter(user=request.user, date_time__gte=fromDateString,date_time__lte=toDateString).all()
    #else: 

    #a graph with number of expenses too
    #all expenses in year distribution

    categoryAmountDict = {}
    print ("all expenses in 1 month")
    for expense in allExpensesForUser:
        print(expense.title, expense.year(),"-",expense.month())
        if expense.categoryValue not in categoryAmountDict:
            categoryAmountDict[expense.categoryValue] = expense.amount
        else: 
            categoryAmountDict[expense.categoryValue] += expense.amount

    for item in categoryAmountDict.items():
        print (item)
    return JsonResponse(categoryAmountDict)

@login_required(login_url="/accounts/login")
def monthAmountStat(request):
    print ("---------> in monthAmountStat")
    print("from request year: ",request.GET["year"])
    yearString = str(request.GET["year"])

    fromDateString = yearString+"-01-01 00:00:00"
    toDateString = str(int(yearString)+1)+"-01-01 00:00:00"
    allExpensesForUser = Expense.objects.filter(user=request.user, date_time__gte=fromDateString,date_time__lte=toDateString).all()
    
    monthAmountDict = {}
    for expense in allExpensesForUser:
        print(expense.title, expense.amount,expense.monthName())
        if expense.monthName() not in monthAmountDict:
            monthAmountDict[expense.monthName()] = expense.amount
        else: 
            monthAmountDict[expense.monthName()] += expense.amount

    for item in monthAmountDict.items():
        print (item)
    return JsonResponse(monthAmountDict)