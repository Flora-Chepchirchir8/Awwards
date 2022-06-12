from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Rating,Projects,Profile

class RatingsForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['design_rating', 'usability_rating', 'content_rating']

class ProjectsForm(forms.ModelForm):
    class Meta:
       model = Projects
       fields = ['title', 'project_image', 'user','description','link','technologies_used','location']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'contact', 'bio', 'image']
      