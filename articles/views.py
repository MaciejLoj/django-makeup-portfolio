from django.shortcuts import render


# Create your views here.

def portfolio(request):
    return render(request,'articles/sesja.html')

def homepage(request):
    return render(request,'homepage.html')
    #return HttpResponse('homepage')