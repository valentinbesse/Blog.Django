import datetime
from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from .forms import CommentForm

# Create your views here.
def list_articles(request):
    articles = Article.objects.all()
    return render(request, 'list_articles.html', {'articles': articles})

def detail_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.published_date = datetime.today().date()
            comment.save()
            return redirect('detail_article', article_id=article.id)
    else:
        form = CommentForm()
    return render(request, 'detail_article.html', {'article': article, 'form': form})