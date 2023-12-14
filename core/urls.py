from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from core.views import PostDetail
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('search/', views.search, name='search'),
    path('category/<int:category_id>', views.category_browse, name='category-browse'),
    path('add_post/', views.add_post, name='add-post')

              ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)