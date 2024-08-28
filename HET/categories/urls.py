from django.urls import path
from . import views

app_name = 'categories'

urlpatterns = [
    path('categories/', views.categories_form, name='categories_form'),
]
