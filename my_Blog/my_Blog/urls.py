
from django.contrib import admin
from django.urls import path
from posts.views import *

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name='index'),
    path('detail/<int:id>', detail, name='detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
