from django.shortcuts import render
import csv
from django.conf import settings


def stations_view(request):
    with open(settings.BUS_STATION_CSV, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        stations = list(reader)

    page = int(request.GET.get('page', 1))
    per_page = 10

    total = len(stations)
    total_pages = (total // per_page) + (1 if total % per_page else 0)

    # защита
    if page < 1:
        page = 1
    if page > total_pages:
        page = total_pages

    start = (page - 1) * per_page
    end = start + per_page

    context = {
        'bus_stations': stations[start:end],
        'page': page,
        'total_pages': total_pages
    }

    return render(request, 'stations/index.html', context)
