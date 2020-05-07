from django.db import models

from django.contrib.auth.models import User
from categories.models import Category
from payment_methods.models import PaymentMethod



DEFAULT_CATEGORY_PK = 5 #other category
DEFAULT_PAYMENT_METHOD_PK=4 #other payment method
class Expense (models.Model):
    #primary key -- id provided automatically by django
    title = models.CharField(max_length = 60)
    body = models.TextField(max_length=512)
    date_time = models.DateTimeField()
    amount = models.FloatField(default=0.0)

    #non final
    currency = models.CharField(max_length=3, default = 'USD')
    category = models.ForeignKey(Category, default = DEFAULT_CATEGORY_PK , on_delete=models.SET_DEFAULT)
    payment_method = models.ForeignKey(PaymentMethod, default = DEFAULT_PAYMENT_METHOD_PK , on_delete=models.SET_DEFAULT)

    # payment_method = models.CharField(max_length=30)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__ (self):
        return "{} (pk={})".format(self.title, self.pk)

    def summary (self):
        return self.body[:100]

    def date_formatted (self):
        return self.date_time.strftime("%b %e %Y")

    def month (self):
        return self.date_time.strftime("%m")

    def monthName (self):
        return self.date_time.strftime("%B")

    def year (self):
        return self.date_time.strftime("%Y")

    #to have access to field inside foreignkey object
    @property
    def categoryValue (self):
        return self.category.value

    @property
    def paymentMethodValue (self):
        return self.payment_method.value



    
