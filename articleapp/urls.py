from articleapp.views import ArticleListView, ArticleUpdateView
from articleapp.views import ArticleCreateView, ArticleDetailView, ArticleDeleteView
from django.urls import path
from django.views.generic.base import TemplateView

app_name = 'articleapp'

urlpatterns = [
    path('list/', ArticleListView.as_view(), name='list'),
    path('create/', ArticleCreateView.as_view(), name='create'),
    path('detail/<int:pk>', ArticleDetailView.as_view(), name='detail'),
    path('update/<int:pk>', ArticleUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', ArticleDeleteView.as_view(), name='delete'),
]