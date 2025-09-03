from django import forms
from .models import Students

class studentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['name', 'email', 'roll', 'fav_sub']