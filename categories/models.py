from django.db import models

from django.contrib.auth.models import User

# Create your models here.

#default categories for all users are categories added by the admin user. Can also be implemented as categories with user set to null

class Category (models.Model):
    value = models.CharField(max_length=35)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__ (self):
        return "{} (pk={}, user={})".format(self.value, self.pk,self.user)
