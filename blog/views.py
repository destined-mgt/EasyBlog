from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from blog.models import Article


class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'article_list'
    model = Article

#class ArticleDetail(generic.DeleteView):
