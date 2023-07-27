from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateTask(forms.Form):
    title = forms.CharField(label="Title", max_length=100)
    description = forms.CharField(
        label="Description", widget=forms.Textarea, max_length=100, required=False
    )


class CreateProject(forms.Form):
    name = forms.CharField(label="Title", max_length=100)


class UpdateProject(forms.Form):
    name = forms.CharField(label="Name", max_length=100)


class CreateUser(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
