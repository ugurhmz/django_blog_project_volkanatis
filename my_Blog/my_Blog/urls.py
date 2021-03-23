
from django.contrib import admin
from django.urls import path
from posts.views import *

from django.conf.urls.static import static
from django.conf import settings

from users.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name='index'),
    path('detail/<int:id>', detail, name='detail'),
    path('delete/<int:id>', delete_post, name='delete'),
    path('update/<int:id>', update_post, name='update'),
    path('create/', create_post, name='create'),
    path('login/',login_view, name='login'),
    path('register/',register_view, name='register'),
    path('logout/',logout_view, name='logout')


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
