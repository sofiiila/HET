from django.urls import path
from . import views

app_name = 'categories'

urlpatterns = [
    path('form/', views.categories_form, name='categories_form'),
]
