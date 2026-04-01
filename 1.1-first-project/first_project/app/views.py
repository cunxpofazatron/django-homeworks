from django.http import HttpResponse
from django.shortcuts import render
import os
from datetime import datetime


def home_view(request):
    pages = [
        {"url": "/current_time/", "name": "Текущее время"},
        {"url": "/workdir/", "name": "Рабочая директория"},
    ]
    return render(request, "home.html", {"pages": pages})


def current_time_view(request):
    now = datetime.now()
    return HttpResponse(f"Текущее время: {now}")


def workdir_view(request):
    files = os.listdir(".")
    return HttpResponse("<br>".join(files))
