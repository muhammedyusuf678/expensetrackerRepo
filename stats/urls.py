from django.urls import path, include
from . import views



urlpatterns = [
    #<int:user_id>
    path('', views.statsIndex, name='statsIndex'),
    path('categoryAmountStat', views.categoryAmountStat),
    path('monthAmountStat', views.monthAmountStat),
    path('paymentMethodAmountStat', views.paymentMethodAmountStat),


]
