from django.urls import path
from .views import list_carros

urlpatterns = [
    path('', list_carros)
]
