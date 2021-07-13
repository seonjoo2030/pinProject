from profileapp.forms import ProfileCreationForm
from django.urls.base import reverse_lazy
from profileapp.models import Profile
from django.shortcuts import render
from django.views.generic.edit import CreateView

class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/create.html'

# models.py 에 정의한 user 객체에 연결해주기 위한 부분. ProfileCreationForm에 user 를 넣지 않은 이유는, 다른 유저가 변경할 수 있는 것을 방지하기 위함.
# form 매개변수에 위에 form_class 로 날라온 데이터들이 들어 있다. 
# commit=False로 해서 임시로 저장. DB에 적용하지 않은 상태

    def form_valid(self, form): 
        temp_profile = form.save(commit=False)
        temp_profile.user = self.request.user
        temp_profile.save()
        return super().form_valid(form)
# Create your views here.
