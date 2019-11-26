from django import forms
from posts.models import project, Services
from django.core.exceptions import ValidationError

class createProject(forms.ModelForm):

    class Meta:
        model = project
        fields = ('title','language','description','published_date','repository')


class CreateService(forms.ModelForm):

    class Meta:
        model = Services
        fields = ('title','description','price')
