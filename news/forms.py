from django import forms
from .models import Post
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm
from django.contrib.auth.forms import UserChangeForm

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class CustomSignupForm(SignupForm):
    username = forms.CharField(max_length=30, label='Username')
    email = forms.EmailField(max_length=30, label='Email')
    password1 = forms.CharField(widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.save()
        return user


class ChangeUsernameForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists.")
        return username

class ChangeEmailForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists.")
        return email

class DeleteAccountForm(forms.Form):
    confirm = forms.BooleanField(label='I confirm that I want to delete my account')