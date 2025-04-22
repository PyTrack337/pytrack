from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    is_premium = forms.BooleanField(required=False, initial=False)

    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2", "is_premium")
        

class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'avatar'] 

    avatar = forms.ImageField(required=False)