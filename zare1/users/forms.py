from django import forms
from codes.models import Code
from users.models import CustomUser
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm


class RegisterForm(forms.Form):
    phonenumber = forms.CharField(max_length=11,help_text='Enter 11 digits phone number')
    #class Meta:
       # model=CustomUser
       # fields=('phonenumber',)








