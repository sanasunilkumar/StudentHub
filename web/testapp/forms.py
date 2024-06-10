from django.contrib.auth.models import User
from django import forms
from testapp.models import Empmodel


class Empforms1(forms.ModelForm):
    class Meta:
        model = Empmodel
        fields = ['name', 'type']


class Empforms(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
