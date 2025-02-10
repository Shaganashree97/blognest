from django import forms
from .models import BlogPost

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

class BlogPostForm(forms.ModelForm):
    class Meta:
        model=BlogPost
        fields=['title','content','image','video']

User = get_user_model()
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
