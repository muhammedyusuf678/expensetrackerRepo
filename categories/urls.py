from django.urls import path, include
from . import views



urlpatterns = [
    #<int:user_id>
    path('', views.allCategories, name='allCategories'),
    path('add', views.addCategory, name='addCategory'),
    path('edit/<int:category_id>', views.editCategory, name='editCategory'),
    path('delete/<int:category_id>', views.deleteCategory, name='deleteCategory'),

]
