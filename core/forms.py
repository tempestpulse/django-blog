from django import forms
from django.forms import ModelForm
from . models import Post
from ckeditor.widgets import CKEditorWidget
class PostForm(ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Post
        fields = ['title', 'overview', 'content', 'category', 'thumbnail']