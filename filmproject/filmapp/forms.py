from django import forms
from.models import Film

class Filmform(forms.ModelForm):
    class Meta:
        model=Film
        fields=['name','description','year','image']

