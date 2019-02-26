
from django.contrib import admin
from django.urls import path
from articles.views import portfolio, homepage, about
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name="homepage"),
    path('portfolio/', portfolio, name="portfolio"),
    path('about-me/', about, name="about")
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)