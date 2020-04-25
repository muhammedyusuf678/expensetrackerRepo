from django.urls import path, include
from . import views



urlpatterns = [
    #<int:user_id>
    path('', views.home, name='home'),
    path('add', views.addExpense, name='addExpense'),
    path('delete/<int:expense_id>', views.deleteExpense, name='deleteExpense'),
    path('edit/<int:expense_id>', views.editExpense, name='editExpense'),

]
