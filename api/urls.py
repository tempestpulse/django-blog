from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('post/', views.PostList.as_view(), name='post-list'),
    path('post/<int:pk>', views.PostDetail.as_view(), name='post-detail'),
    path('category/', views.CategoryList.as_view(), name='category-list'),
    path('category/<int:pk>', views.CategoryDetail.as_view(), name='category-detail'),
    path('comment/', views.CommentList.as_view(), name='comment-list'),
    path('comment/<int:pk>', views.CommentDetail.as_view(), name='comment-detail')
]