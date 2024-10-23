from django.urls import path
from .templates.views import PostListView, PostCreateView, PostDeleteView, PostUpdateView, PostDetailView
from .templates import views

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post-create', PostCreateView.as_view(), name='post-create'),
    path('post-detail/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post-update/<int:pk>', PostUpdateView.as_view(), name='post-update'),
    path('post-delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
]