from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, Pattern


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'profile_image')


class PatternForm(forms.ModelForm):
    class Meta:
        model = Pattern
        fields = ('title',)
