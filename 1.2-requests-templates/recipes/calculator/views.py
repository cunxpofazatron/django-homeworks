from django.shortcuts import render


def recipes_view(request):
    recipes = {
        'omelette': ['яйца', 'молоко', 'соль'],
        'pasta': ['макароны', 'сыр'],
    }

    dish = request.GET.get('dish')

    context = {
        'recipe': recipes.get(dish)
    }

    return render(request, 'calculator/index.html', context)

