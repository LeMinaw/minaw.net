#-*- coding: utf-8 -*-

from django import forms

class NewImageForm(forms.Form): # TODO: Strong form validation, mind to reject URLs from DynImg to avoid endless loops !
    name       = forms.CharField    (required=False, label="Nom de l'image dynamique")
    urls       = forms.CharField    (required=True,  label="URLs des images (une URL par ligne)", widget=forms.Textarea)
    shadowMode = forms.BooleanField (required=False, label="Mode discret")
