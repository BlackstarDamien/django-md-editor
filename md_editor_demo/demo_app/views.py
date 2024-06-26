from django.shortcuts import render
from .models import Article


def index(request):
    articles = Article.objects.all()
    context = {"articles": articles}
    return render(request, "index.html", context=context)

def article(request, id):
    article = Article.objects.get(id=id)
    return render(request, "article.html", {"article": article})
