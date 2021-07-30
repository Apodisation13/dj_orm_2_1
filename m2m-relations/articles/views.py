from django.shortcuts import render
from django.views.generic import ListView

from articles.models import *


# 1й способ - на функции
def articles_list(request):
    template = 'articles/article_list.html'
    articles = Article.objects.all().prefetch_related('t1', 't1__tag')

    context = {
        'object_list': articles,
        }

    return render(request, template, context)


# 2й способ - на классе
class ArticleView(ListView):
    model = Article
    template_name = 'articles/news.html'

    def get_queryset(self):
        return Article.objects.all().prefetch_related('t1', 't1__tag')
