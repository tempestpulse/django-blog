from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from core.views import PostDetail
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post-detail')

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)