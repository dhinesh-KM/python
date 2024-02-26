from typing import Any
from django import forms
from .models import CustomUser

class UserRegistrationForm(forms.ModelForm):
    choices = [
        ("M","Male"),
        ("F","Female"),
        ("O","Others")
    ]
    gender = forms.ChoiceField(choices=choices)
    password = forms.CharField(widget=forms.PasswordInput)
    confirmpassword = forms.CharField(widget=forms.PasswordInput,label='Confirm Password')
    
    
    class Meta:
        model = CustomUser
        fields = ['username','email','password','confirmpassword','gender']
        help_texts = {
            'username': '',
        }
    
    def clean(self) -> dict[str, Any]:
        cleaned_data = super().clean()
        p1 = cleaned_data.get("password")
        p2 = cleaned_data.get("confirmpassword")
        if p1 != p2:
            raise forms.ValidationError("password doesn't match")
        return cleaned_data
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError("Username is already taken.")
        return username
        

class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)