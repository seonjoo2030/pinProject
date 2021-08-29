from articleapp.models import Article
from django.views.generic.list import MultipleObjectMixin
from accountapp.decorators import account_ownership_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from accountapp.forms import AccountUpdateForm
from django.contrib.auth.admin import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.urls.base import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView

from accountapp.models import HelloWorld

has_ownership = [login_required, account_ownership_required]

@login_required                                 #login authenticated 관련 decorator login 여부 확인, 처리
def Hello_World(request):
    if request.method == "POST":
        temp = request.POST.get('hello_world_input')
        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()

        return render(request, "accountapp/hello_world.html", context={'hello_world_list': hello_world_list})


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user'    #detail/<int:pk> 에서 pk 부분의 값을 가져오게 된다.
    template_name = 'accountapp/detail.html'

    paginate_by = 25

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object())
        return super(AccountDetailView, self).get_context_data(object_list=object_list, **kwargs)

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/delete.html'