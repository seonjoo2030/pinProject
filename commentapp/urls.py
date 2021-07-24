from commentapp.views import CreateCommentView
from django.urls.conf import path

app_name = 'commentapp'

urlpatterns = [
    path('create/', CreateCommentView.as_view(), name='create'),
]