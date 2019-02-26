from django.shortcuts import render



def portfolio(request):
    return render(request,'articles/sesja.html')


def homepage(request):
    return render(request,'homepage.html')


def about(request):
    return render(request,'articles/about.html')
