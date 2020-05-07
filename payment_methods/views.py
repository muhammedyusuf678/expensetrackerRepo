from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required

# Create your views here.

from .models import PaymentMethod

from datetime import datetime

@login_required(login_url="/accounts/login")
def allPaymentMethods (request):
    allPaymentMethodsForUser = PaymentMethod.objects.filter(user=request.user)
    defaultPaymentMethods = PaymentMethod.objects.filter(user=1) #set by admin user

    return render(request,"payment_methods/allPaymentMethods.html",{"paymentMethods":allPaymentMethodsForUser, 'defaultPaymentMethods':defaultPaymentMethods})

@login_required(login_url="/accounts/login")
def addPaymentMethod (request):
    if request.method == 'POST':
        if request.POST['value']:
            newPaymentMethod = PaymentMethod()
            newPaymentMethod.value = request.POST['value']
            newPaymentMethod.user = request.user
            newPaymentMethod.save()
            return redirect('allPaymentMethods')
    else: 
        return render(request,'payment_methods/addPaymentMethod.html')


def editPaymentMethod (request, payment_method_id):
    paymentMethodToEdit = PaymentMethod.objects.get(pk=payment_method_id)
    if request.method == 'POST':
        if request.POST['value']:
            paymentMethodToEdit.value = request.POST['value']
            paymentMethodToEdit.save()
            return redirect('allPaymentMethods')
    else: 
        return render(request,'payment_methods/editPaymentMethod.html',{'paymentMethod':paymentMethodToEdit})

def deletePaymentMethod (request, payment_method_id):
    PaymentMethod.objects.get(pk=payment_method_id).delete()
    return redirect('allPaymentMethods')



