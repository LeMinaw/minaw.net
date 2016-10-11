#-*- coding: utf-8 -*-

from django import forms

class NewImageForm(forms.Form): # TODO: Strong form validation, mind to reject URLs from DynImg to avoid endless loops !
    name       = forms.CharField    (required=False, label="Dynamic image name")
    urls       = forms.CharField    (required=True,  label="Images URLs (one url per line)", widget=forms.Textarea)
    shadowMode = forms.BooleanField (required=False, label="Shadow copy mode")
