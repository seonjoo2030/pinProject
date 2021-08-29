from projectapp.models import Project
from django.forms.models import ModelForm


class ProjectCreationForm(ModelForm):
    class Meta:
        model = Project
        fields = ['image', 'title', 'description']