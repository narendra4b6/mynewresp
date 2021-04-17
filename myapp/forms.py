from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from myapp.models import Post,Comment



class SignUpForm(UserCreationForm):
    first_name=forms.CharField(required=True)
    last_name=forms.CharField(required=True)
    email=forms.EmailField(required=True)
    gen=[('male','Male'),('female','Female')]
    gender=forms.ChoiceField(choices=gen,widget=forms.RadioSelect(),required=True)
    class Meta:
        model=get_user_model()
        fields=('first_name','last_name','gender','email','username','password1','password2')

class PostForm(forms.ModelForm):
    class Meta():
        model=Post
        fields=('title','text','picture')

class CommentForm(forms.ModelForm):
    class Meta():
        model=Comment
        fields=('author','text')
