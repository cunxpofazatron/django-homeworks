from .views import catalog, phone
from django.urls import path

urlpatterns = [
    path('', catalog, name='catalog'),
    path('<slug:slug>/', phone, name='phone'),
]
