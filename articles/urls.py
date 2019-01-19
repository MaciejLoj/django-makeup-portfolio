
from django.urls import path
from firstapp.views import about, homepage
from articles.views import article_list

urlpatterns = [
    path('', article_list),
    path('', homepage),
]
