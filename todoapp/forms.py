from django import forms

class CreateTask(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    description = forms.CharField(label='Description', widget=forms.Textarea, max_length=100, required=False)

class CreateProject(forms.Form):
    name = forms.CharField(label='Title', max_length=100)
