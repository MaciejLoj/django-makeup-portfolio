
from django.contrib import admin
from django.urls import path, include
from firstapp.views import about, homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about),
    path('', homepage),
    path('articles/', include('articles.urls')),
]

