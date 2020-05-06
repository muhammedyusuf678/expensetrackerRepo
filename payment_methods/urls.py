from django.urls import path, include
from . import views


urlpatterns = [
    #<int:user_id>
    path('', views.allPaymentMethods, name='allPaymentMethods'),
    path('add', views.addPaymentMethod, name='addPaymentMethod'),
    path('edit/<int:payment_method_id>', views.editPaymentMethod, name='editPaymentMethod'),
    path('delete/<int:payment_method_id>', views.deletePaymentMethod, name='deletePaymentMethod'),

]
