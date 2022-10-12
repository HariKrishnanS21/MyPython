from .models import todo
from django import forms

class tform(forms.ModelForm):
    class Meta:
        model=todo
        fields=['task','prio','date']