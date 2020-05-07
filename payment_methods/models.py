from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class PaymentMethod (models.Model):
    value = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__ (self):
        return "{} (pk={}, user={})".format(self.value, self.pk,self.user)