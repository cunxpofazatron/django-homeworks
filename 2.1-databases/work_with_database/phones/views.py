from django.shortcuts import render, get_object_or_404
from .models import Phone


def catalog(request):
    phones = Phone.objects.all()

    sort = request.GET.get('sort')

    SORT_MAP = {
        'name': 'name',
        'min_price': 'price',
        'max_price': '-price',
    }

    if sort in SORT_MAP:
        phones = phones.order_by(SORT_MAP[sort])

    return render(request, 'catalog.html', {
        'phones': phones
    })


def phone(request, slug):
    phone = get_object_or_404(Phone, slug=slug)

    return render(request, 'phone.html', {
        'phone': phone
    })
