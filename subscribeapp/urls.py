from subscribeapp.views import SubscriptionView
from django.urls.conf import path

app_name = 'subscribeapp'

urlpatterns = [
    path('subscribe/', SubscriptionView.as_view(), name='subscribe'),
]