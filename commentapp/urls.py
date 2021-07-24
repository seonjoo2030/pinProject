from commentapp.views import CreateCommentView, DeleteCommentView
from django.urls.conf import path

app_name = 'commentapp'

urlpatterns = [
    path('create/', CreateCommentView.as_view(), name='create'),
    path('delete/<int:pk>', DeleteCommentView.as_view(), name='delete'),
]