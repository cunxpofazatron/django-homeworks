import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')
django.setup()

from articles.models import Article


def show_articles():
    for article in Article.objects.all():
        print(article.title)
        for tag in article.tags.all():
            print(f"  - {tag.name}")


if __name__ == "__main__":
    show_articles()
