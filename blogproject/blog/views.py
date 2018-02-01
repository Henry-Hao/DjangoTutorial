from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article, Category
import markdown, pygments
# Create your views here.

def index(request):
    articles = Article.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'articles':articles})

def archives(request, year, month):
    articles = Article.objects.filter(created_time__year=year,created_time__month=month).order_by("-created_time")
    return render(request, 'blog/index.html', context={'articles':articles})

def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    articles = Article.objects.filter(category=cate).order_by("-created_time")
    return render(request, 'blog/index.html', context={'articles':articles})

def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.text = markdown.markdown(article.text, ['extra', 'codehilite', 'toc'])
    return render(request, 'blog/detail.html', context={'article': article})
