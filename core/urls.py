from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.log_in, name='login'),
    path('logout', views.log_out, name='logout'),
    path('register/', views.register, name='register'),
    path('post/<int:pk>/', views.post_detail, name='post-detail'),
    path('search/', views.search, name='search'),
    path('category/<int:category_id>', views.category_browse, name='category-browse'),
    path('add_post/', views.add_post, name='add-post')

              ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)