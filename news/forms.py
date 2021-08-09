from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import News,Tag



class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = ('title', 'text', 'img', 'tag')
        
        widgets = {
        'title': forms.TextInput(attrs={'class':'form-control'}),
        'text': forms.Textarea(attrs={'class':'form-control'}),
        'img': forms.URLInput(attrs={'class':'form-control'}),
        }

class NewsFormTag(forms.ModelForm):

    class Meta:
        model = Tag
        fields = ('name',)
 
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
        }
