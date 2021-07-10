from accountapp.views import AccountCreateView, Hello_World
from django.urls import path, include


app_name = "accountapp"

urlpatterns = [
    path('hello_world/', Hello_World, name="hello_world"),
    path('create/', AccountCreateView.as_view(), name="create"),
]