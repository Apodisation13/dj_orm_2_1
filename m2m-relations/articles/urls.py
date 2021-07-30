from django.urls import path

from articles.views import *

urlpatterns = [
    path('', ArticleView.as_view(), name='articles'),
]
