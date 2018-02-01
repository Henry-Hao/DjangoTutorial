from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article, Category
from comments.forms import CommentForm
import markdown, pygments
# Create your views here.

def index(request):
    articles = Article.objects.all()
    return render(request, 'blog/index.html', context={'articles':articles})

def archives(request, year, month):
    articles = Article.objects.filter(created_time__year=year,created_time__month=month)
    return render(request, 'blog/index.html', context={'articles':articles})

def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    articles = Article.objects.filter(category=cate)
    return render(request, 'blog/index.html', context={'articles':articles})

def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.text = markdown.markdown(article.text, ['extra', 'codehilite', 'toc'])
    form = CommentForm()
    comment_list = article.comment_set.all().order_by("-created_time")
    context = {
        'article':article,
        'form':form,
        'comment_list':comment_list
    }
    return render(request, 'blog/detail.html', context=context)
