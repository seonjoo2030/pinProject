from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include, path

from accountapp.views import AccountCreateView, AccountDetailView, AccountUpdateView, Hello_World

app_name = "accountapp"

urlpatterns = [
    path('hello_world/', Hello_World, name="hello_world"),
    path('create/', AccountCreateView.as_view(), name="create"),
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('detail/<int:pk>', AccountDetailView.as_view(), name="detail"),
    path('update/<int:pk>', AccountUpdateView.as_view(), name="update"),
]