from django.shortcuts import render
from articles.models import Article
from django.http import HttpResponse

# Create your views here.

def article_list(request):
    artic = Article.objects.all().order_by('date')
    return render(request,'articles/articles.html', {'articles': artic })


def article_detail(request, slug):
    #znajdz taki artykul ktorego slug = wyswietlonemu w url slugowi
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html',{'article': article})
    #return HttpResponse(slug)