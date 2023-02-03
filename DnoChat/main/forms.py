from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm, TextInput
from .models import Messages


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class FindUsers(forms.Form):
    name = forms.CharField(max_length=30)


class Messanger(ModelForm):
    class Meta:
        model = Messages
        fields = ['message']

        widgets = {
            "message": TextInput(attrs={'class': 'form-control', 'placeholder': "Сообщение"})
        }
