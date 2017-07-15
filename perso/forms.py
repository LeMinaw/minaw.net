#-*- coding: utf-8 -*-

from django       import forms
from perso.models import *

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['email']
        error_messages = {
            'email': {
                'unique': "Cette adresse email est déjà enregistrée !"
            }
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['pseudo', 'email', 'content', 'publi']
        widgets = {'publi': forms.HiddenInput()}
        labels = {
            'pseudo': "Nom ou pseudo",
            'email': "Adresse e-mail (facultative)",
            'content': "Votre commentaire"
        }
