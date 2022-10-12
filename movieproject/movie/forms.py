from django import forms
from .models import movie
class movform(forms.ModelForm):
    class Meta:
        model=movie
        fields=['desc']