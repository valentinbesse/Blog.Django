from django.shortcuts import render, get_object_or_404, redirect
from .models import Article

# Create your views here.
def list_articles(request):
    articles = Article.objects.all()
    return render(request, 'articles/list_articles.html', {'articles': articles})

def detail_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'articles/detail_article.html', {'article': article})