from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model=Article
        fields=['title']
        
    
class ArticleFormOld(forms.Form):
    title=forms.CharField()
    content=forms.CharField()
    
    def clean_title(self):
        cleaned_data=self.cleaned_data
        print("cleaned_data",cleaned_data)
        title=cleaned_data.get('title')
        
        print("title",title)
        return title
    
    