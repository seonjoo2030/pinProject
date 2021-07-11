from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    #profile과 유저 객체를 하나 씩 연결해준다.
    #on_delete는 연결된 유저 객체가 delete 될 때, 그와 연결된 Profile 객체가 어떤 행동을 할 것인지 정의하는 부분이다.
    # CASCADE는 유저 객체가 delete 될 때, Profile 객체도 delete 되도록 하는 것이다. 장고 문서 참고
    # relate_name 이라는 것은 request.user.* 이런 형식에서 유저 객체의 데이터를 가져오는데, 이때 참고할 것을 정하는 것이다. 
    # 여기서는 request.user.profile이 될 것이고, 'nickname'이라고 설정한다면, request.user.nickname 을 참조 할 것이다.
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')  

    # upload_to 라는 것은 서버 내에 어디에 이미지 파일이 저장 될 것인지 설정하는 것이다. media/profile/ 하위 경로로 저장될 것이다. 
    image = models.ImageField(upload_to='profile/', null=True)

    nickname = models.CharField(max_length=20, unique=True, null=True)

    message = models.CharField(max_length=100, null=True)
# Create your models here.
