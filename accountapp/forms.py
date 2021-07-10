from django.contrib.auth.forms import UserCreationForm

class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)       ## 파이썬 초기화 관련 부분 확인, 학습 필요

        self.fields['username'].disabled = True