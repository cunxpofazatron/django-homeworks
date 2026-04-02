from django.urls import path
from .views import stations_view

urlpatterns = [
    path('', stations_view),
]
