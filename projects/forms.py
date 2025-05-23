from django import forms
from .models import Project, Attachment
# from django.contrib.auth.models import User
from tempus_dominus.widgets import DatePicker
from teams.models import Team
from .utils import STATUS_CHOICES, PRIORITY_CHOICES

class ProjectForm(forms.ModelForm):
    description= forms.CharField(
        widget = forms.Textarea(
            attrs ={'rows':3, 'placeholder': "Describe your project .."}
        ),
        label=False,
        required=True
    )
    
    
    name = forms.CharField(
        widget = forms.TextInput(
            attrs ={'placeholder': "Enter the project name .."}
        ),
        required=True,
        label=False
    )
    
    # owner = forms.ModelChoiceField(
    #     queryset=User.objects.filter(is_active=True),
    #     widget =forms.Select(
    #         attrs ={'class':'form-control'}
    #     ),
    #     label =False,
    #     required=True
    # )
    
    team = forms.ModelChoiceField(
        queryset=Team.objects.all(),
        widget =forms.Select(
            attrs ={'class':'form-control'}
        ),
        label =False,
        required=True
    )
    
    client_company = forms.CharField(
        label ='',
        required=True
    )
    
    total_amount = forms.DecimalField(
        label =False,
        required=False
    )
    
    
    amount_spent = forms.DecimalField(
        label =False,
        required=False
    )
    
    estimated_duration = forms.DecimalField(
        label =False,
        required=False
    )
    
    
    status = forms.ChoiceField(
        choices =STATUS_CHOICES,
        widget =forms.Select(
            attrs ={'class':'form-control'}
        ),
        label ='',
        required=True
    )
    
    
    priority = forms.ChoiceField(
        choices =PRIORITY_CHOICES,
        widget =forms.Select(
            attrs ={'class':'form-control'}
        ),
        label ='',
        required=True
    )
    
    
    
    start_date = forms.DateTimeField(
        label='',
        required=True,
        widget=DatePicker(
            attrs = {
                'append': 'fa fa-calendar',
                'icon_toggle':True,
            }
        )
    )
    
    
    due_date = forms.DateTimeField(
        label='',
        required = True,
        widget=DatePicker(
            attrs = {
                'append': 'fa fa-calendar',
                'icon_toggle':True,
            }
        )
    )
    
    
    class Meta:
        model = Project
        fields = [
            "name",
            "team",
            "description",
            "status",
            "priority",
            "start_date",
            "due_date",
            "client_company",
            "total_amount",
            "amount_spent",
            "estimated_duration"]
        
class AttachmentForm(forms.ModelForm):
    class Meta:
        model = Attachment
        fields =['file'] 