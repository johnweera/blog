from django.urls import path
from django.views.generic import TemplateView
from .views import PostListView, PostDetailView, AuthorPostListView, PostUpdateView, PostDeleteView
from . import views

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('add/', views.create_post, name='add'),
    path('author/', AuthorPostListView.as_view(), name='author'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),
]