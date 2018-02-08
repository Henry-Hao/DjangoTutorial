from django.conf.urls import url

from . import views
# add routers
app_name = 'blog'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.ArticleDetailView.as_view(), name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name="archives"),
    url(r'^post/category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name="category")
]
