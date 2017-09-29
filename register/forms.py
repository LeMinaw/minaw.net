from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(required=True, max_length=255, label="Forum username")
    code     = forms.CharField(required=True, max_length=255, label="Activation code")
