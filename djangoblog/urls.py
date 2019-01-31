
from django.contrib import admin
from django.urls import path, include
from articles.views import portfolio, homepage
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name="homepage"),
    path('portfolio/', portfolio, name="portfolio"),
]

#This will return the proper URL pattern for serving
# static files to your already defined pattern list.
urlpatterns += staticfiles_urlpatterns()
# django is going to set up a url for us
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)