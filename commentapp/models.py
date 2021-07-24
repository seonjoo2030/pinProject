from django.contrib.auth.models import User
from django.db import models
from articleapp.models import Article


class Comment(models.Model):
    # related_name은 django의 ORM을 위함. article, user 객체에서 Comment model에 대한 접근할 때, user.comment.all() 이렇게
    # user의 어떤 내용을 가져올 것인가 직관적으로 볼 수 있다. 
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True, related_name='comment')
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comment')

    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now=True)
# Create your models here.
