from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required

# Create your views here.

from .models import Expense
from categories.models import Category
from payment_methods.models import PaymentMethod


from datetime import datetime, date

@login_required(login_url="/accounts/login")
def home (request):
    print("----------------> Current user id: ",request.user.id)
    print (request.GET)
    fromYearAndMonthString = ""
    if 'fromDate' and 'toDate' in request.GET:
        print ('fromDate and toDate are there')
        fromYearAndMonthString = str(request.GET['fromDate'])
        toYearAndMonthString = str(request.GET['toDate'])
    else: 
        print ('fromDate and toDate are NOT there')
        fromYearAndMonthString = date.today().strftime('%Y-%m')
        splittedFromYearAndMonth = fromYearAndMonthString.split("-")
        year = splittedFromYearAndMonth[0]
        month = splittedFromYearAndMonth[1]
        toYearAndMonthString = year+"-0"+str(int(month)+1)
    
    fromDateString = fromYearAndMonthString+"-01 00:00:00"
    toDateString = toYearAndMonthString+"-01 00:00:00"

    allExpensesForUser = Expense.objects.filter(user=request.user.id, date_time__gte=fromDateString,date_time__lte=toDateString).order_by('-date_time')

    selectedCategoryPK = -1
    if 'category' in request.GET:
        selectedCategoryPK = request.GET['category']
        if int(selectedCategoryPK) != -1:
            categoryFilter = Category.objects.get(pk=selectedCategoryPK)
            print(categoryFilter)
            #add filter to query set produced
            allExpensesForUser = allExpensesForUser.filter(category = categoryFilter).order_by('-date_time')
    
    selectedPaymentMethodPK = -1
    if 'payment_method' in request.GET:
        selectedPaymentMethodPK = request.GET['payment_method']
        if int(selectedPaymentMethodPK) != -1:
            paymentMethodFilter = PaymentMethod.objects.get(pk=selectedPaymentMethodPK)
            print(paymentMethodFilter)
            #add filter to query set produced
            allExpensesForUser = allExpensesForUser.filter(payment_method = paymentMethodFilter).order_by('-date_time')

    searchInput = ''
    if 'searchInput' in request.GET:
        searchInput = request.GET['searchInput']
        titleMatches = allExpensesForUser.filter(title__icontains = searchInput)
        bodyMatches = allExpensesForUser.filter(body__icontains = searchInput)
        allExpensesForUser = titleMatches | bodyMatches
        allExpensesForUser = allExpensesForUser.order_by('-date_time')


    defaultCategories = Category.objects.filter(user=1) #set by admin user
    allCategoriesForUser = Category.objects.filter(user=request.user)

    defaultPaymentMethods = PaymentMethod.objects.filter(user=1) #set by admin user
    allPaymentMethodsForUser = PaymentMethod.objects.filter(user=request.user)
    
    return render(request, 'expenses/home.html',{'expenses':allExpensesForUser,'fromDate':fromYearAndMonthString,'toDate':toYearAndMonthString, 'userCategories':allCategoriesForUser,'defaultCategories':defaultCategories, 'userPaymentMethods':allPaymentMethodsForUser,'defaultPaymentMethods': defaultPaymentMethods, 'selectedCategoryPK':selectedCategoryPK,
    'selectedPaymentMethodPK':selectedPaymentMethodPK,
    'searchInput':searchInput})

@login_required(login_url="/accounts/login")
def addExpense(request):
    print ("----> in addExpense")
    if request.method == "POST":
        #check all required fields
        if request.POST["title"] and request.POST["amount"] and request.POST["payment_method"] and request.POST["body"] and request.POST["category"]:
            newExpense = Expense()
            newExpense.title = request.POST["title"]
            newExpense.amount = request.POST["amount"]
            newExpense.currency = "AED"
            newExpense.body = request.POST["body"]

            selectedCategoryPK = int(request.POST["category"])
            newExpense.category = Category.objects.get(pk=selectedCategoryPK)

            selectedPaymentMethodPK = int(request.POST["payment_method"])
            newExpense.payment_method = PaymentMethod.objects.get(pk=selectedPaymentMethodPK)

            datetime_str = request.POST["date"]+" "+request.POST["time"]
            print(datetime_str)
            datetime_object = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M')
            newExpense.date_time = datetime_object

            newExpense.user = request.user
            newExpense.save()

            return redirect('home')
    else: 
        defaultCategories = Category.objects.filter(user=1) #set by admin user
        allCategoriesForUser = Category.objects.filter(user=request.user)

        defaultPaymentMethods = PaymentMethod.objects.filter(user=1) #set by admin user
        allPaymentMethodsForUser = PaymentMethod.objects.filter(user=request.user)

        return render(request,"expenses/addExpense.html",{'userCategories':allCategoriesForUser,'defaultCategories':defaultCategories, 'userPaymentMethods':allPaymentMethodsForUser,'defaultPaymentMethods': defaultPaymentMethods})

@login_required(login_url="/accounts/login")
def deleteExpense (request, expense_id):
    print("----------------------> in deleteExpense")
    Expense.objects.filter(pk=expense_id).delete()
    return redirect("home")

@login_required(login_url="/accounts/login")
def editExpense (request, expense_id):
    print("----------------------> in editExpense")
    expense = Expense.objects.get(pk=expense_id)

    if request.method == "POST":
        if request.POST["title"] and request.POST["amount"] and request.POST["payment_method"] and request.POST["body"] and request.POST["category"]:
            expense.title = request.POST["title"]
            expense.amount = request.POST["amount"]
            expense.currency = "AED"
            expense.body = request.POST["body"]

            selectedCategoryPK = int(request.POST["category"])
            expense.category = Category.objects.get(pk=selectedCategoryPK)

            selectedPaymentMethodPK = int(request.POST["payment_method"])
            expense.payment_method = PaymentMethod.objects.get(pk=selectedPaymentMethodPK)

            datetime_str = request.POST["date"]+" "+request.POST["time"]
            print(datetime_str)
            datetime_object = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M')
            expense.date_time = datetime_object
            #newExpense.user = request.user
            expense.save()
            return redirect('home')
    else: 
        allCategoriesForUser = Category.objects.filter(user=request.user)
        defaultCategories = Category.objects.filter(user=1) #set by admin user

        defaultPaymentMethods = PaymentMethod.objects.filter(user=1) #set by admin user
        allPaymentMethodsForUser = PaymentMethod.objects.filter(user=request.user)

        splitted = expense.date_time.strftime('%Y-%m-%d %H:%M').split()
        date_val = splitted[0]
        time_val = splitted[1]
        return render(request,"expenses/editExpense.html",{'expense':expense,"date_val":date_val,'time_val':time_val, 'userCategories':allCategoriesForUser,'defaultCategories':defaultCategories, 'userPaymentMethods':allPaymentMethodsForUser,'defaultPaymentMethods': defaultPaymentMethods})


