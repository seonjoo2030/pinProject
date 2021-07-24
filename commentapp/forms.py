from commentapp.models import Comment
from django.forms.models import ModelForm


class CommentCreationForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']