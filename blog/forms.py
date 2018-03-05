from django import forms
from .models import Comment

# Form Fields
# https://docs.djangoproject.com/en/1.8/ref/forms/fields/

# Django has Two Base-class to build forms ,
#    -- Form
#    -- ModelForm


class EmailPostForm(forms.Form):
    name = forms.CharField(label='', max_length=25, widget=forms.TextInput(attrs={'placeholder': 'Name:'}))
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'placeholder': 'Email:'}))
    to = forms.EmailField(label='', widget=forms.TextInput(attrs={'placeholder': 'To:'}))
    comments = forms.CharField(required=False, label='', widget=forms.Textarea(attrs={'placeholder': 'Comments:'}))


### Creating Form from models #####
# https://docs.djangoproject.com/en/1.8/topics/forms/modelforms/

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name:'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email:'}),
            'body': forms.Textarea(attrs={'placeholder': 'Comment:'}),
        }
        labels = {
            'name': '',
            'email': '',
            'body': '',
        }


class SearchForm(forms.Form):
    query = forms.CharField()
