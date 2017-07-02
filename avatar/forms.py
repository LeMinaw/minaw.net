#-*- coding: utf-8 -*-

from django import forms

class TestForm(forms.Form):
    email = forms.CharField(required=True, label="Email, pseudo, nom...")
