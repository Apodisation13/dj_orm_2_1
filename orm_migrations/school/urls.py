from django.urls import path

from school.views import *

urlpatterns = [
    path('', StudentView.as_view(), name='students'),
]
