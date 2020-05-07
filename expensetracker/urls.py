from django.contrib import admin
from django.urls import path, include

from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing, name='landing'),
    path('accounts/',include('accounts.urls')),
    path('expenses/',include('expenses.urls')),
    path('categories/',include('categories.urls')),
    path('stats/',include('stats.urls')),
    path('payment_methods/',include('payment_methods.urls')),

]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
