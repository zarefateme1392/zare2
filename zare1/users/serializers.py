from rest_framework import serializers
from django.contrib.auth.models import User
from .models import CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from users.models import *
from users.forms import *
from django import forms
from drf_braces.serializers.form_serializer import FormSerializer
#from rest_framework.permissions import AllowAny
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('phonenumber',)

#class CodeSerializer(FormSerializer):
   # class Meta():
       # form=CodeForm1

class CodeSerializer1(serializers.Serializer):
    number = serializers.CharField()