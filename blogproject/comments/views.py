from django.shortcuts import render, get_object_or_404, redirect
from django.http import request
from blog.models import Article

from .models import Comment
from .forms import CommentForm

# Create your views here.


def post_comment(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # create the instance of Comment according to form without storing into database
            comment = form.save(commit=False)
            comment.article = article
            # now save the instance into database
            comment.save()
            return redirect(article)
        else:
            comment_list = article.comment_set.all()
            context = {
                'article':article,
                'form':form,
                'comment_list':comment_list
            }
            return render(request, 'blog/detail.html', context=context)
        

    else:
        redirect(article)
