from django.shortcuts import render
from .models import Article


def articles_list(request):
    template = 'articles/news.html'

    # Забираем все статьи из базы данных вместе с их связями (тегами),
    # чтобы страница загружалась быстро
    articles = Article.objects.all().prefetch_related('scopes')

    # Передаем статьи в шаблон
    context = {
        'object_list': articles
    }

    return render(request, template, context)
