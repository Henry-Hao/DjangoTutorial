from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article, Category
from comments.forms import CommentForm
import markdown, pygments
from django.views.generic import ListView,DetailView


# Create your views here.


class IndexView(ListView):
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'articles'
    paginate_by = 2

class CategoryView(IndexView):
    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super(CategoryView,self).get_queryset().filter(category=cate)

class ArchivesView(IndexView):
    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        return super(ArchivesView,self).get_queryset().filter(created_time__year=year, created_time__month=month)

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/detail.html'
    context_object_name = 'article'

    def get(self, request, *args, **kwargs):
        super(ArticleDetailClass, self).get(request,*args,**kwargs)
        self.object.increase_views()
        return response

    def get_object(self, queryset=None):
        article = super(ArticleDetailClass,self).get_object(queryset=None)
        article.text = markdown.markdown(article.text,
                ['extra','codehilite','toc'])
        return article


    def get_context_data(self, **kwargs):
        context = super(ArticleDetailClass,self).get_context_data(**kwargs)
        form = CommentForm()
        comment_list = self.object.comment_set.all()
        context.update({
            "form":form,
            "comment_list":comment_list
            })
        return context

