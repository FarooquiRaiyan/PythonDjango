from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    comment =forms.CharField(
        label=False,
        required=True,
        widget=forms.Textarea(
            attrs={'rows':3, 'placeholder':'Add a comment...'}, 
        )
    )
    class Meta:
        model = Comment
        fields = ['comment']
        
    def clean_comment(self):
        comment = self.cleaned_data.get('comment')
        if len(comment) < 6:
            raise forms.ValidationError("Comment Must be atleast 6 characters long")  
        return comment
        
        