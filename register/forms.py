from django import forms

class RegisterForm(forms.Form):
    username = forms.TextField(required=True, max_lenght=255, label="Forum username (exact and case sensitive!)")
    code     = forms.TextField(required=True, max_lenght=255, label="Activation code")
