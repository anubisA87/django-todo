from django import forms

class CreateTask(forms.Form):
    title = forms.CharField(label='Titulo', max_length=100),
    description = forms.CharField(label='Descripcion', widget=forms.Textarea, max_length=100, required=False),