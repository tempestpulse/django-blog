from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('post/', views.PostList.as_view(), name='post-list'),
    path('post/<int:pk>', views.PostDetail.as_view(), name='post-detail'),
]