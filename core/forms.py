from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Post, Comment, User


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'overview', 'content', 'category', 'thumbnail']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Join the discussion and leave a comment...'})
        }


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
