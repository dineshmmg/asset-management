from django import forms
from .models import *
from django.contrib.auth.models import User, auth


    
class userform(forms.ModelForm):
    model = User
    fields = ['first_name', 'last_name', 'username', 'email']