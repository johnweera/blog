from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.AllPostView.as_view(), name = 'index'),
    path('add/', views.PostCreateView.as_view(), name = 'add'),
    path('list/', views.PostListView.as_view(), name = 'list'),
    path('list/<int:pk>/', views.PostDetailView.as_view(), name = 'detail'), 
    path('list/<int:pk>/update/', views.PostUpdateView.as_view(), name = 'update'),
    path('list/<int:pk>/delete/', views.PostDeleteView.as_view(), name = 'delete'),
]