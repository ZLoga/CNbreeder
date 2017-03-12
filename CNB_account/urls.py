# zloga@zloga.com

from django.conf.urls import url
from CNB_account import views

urlpatterns = [
    url(r'^account/login$', views.login),
    url(r'^account/register$', views.register),
    # url(r'^blog/article/(?P<article_id>\d+)$', views.ArticleDetailView.as_view(), name='detail'),
    # url(r'^blog/category/(?P<cate_id>\d+)$', views.CategoryView.as_view(), name='category'),
]