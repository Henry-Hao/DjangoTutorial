from django.conf.urls import url

from . import views
# add routers
urlpatterns = [
    url(r'^$', views.index, name='index'),
]