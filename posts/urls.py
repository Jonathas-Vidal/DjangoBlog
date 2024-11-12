from django.urls import path
from .views import PostListView, PostCreateView, PostDeleteView, PostUpdateView,PostSearchView, PostDetailView, MyPostListView

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('my-posts', MyPostListView.as_view(), name='my-posts'),
    path('post-create', PostCreateView.as_view(), name='post-create'),
    path('post-detail/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/search/', PostSearchView.as_view(), name='post-search'),
    path('post-update/<int:pk>', PostUpdateView.as_view(), name='post-update'),
    path('post-delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
]