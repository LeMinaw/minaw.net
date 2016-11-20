#-*- coding: utf-8 -*-

from django       import forms
from profs.models import *

class ModulesForm(forms.Form): #TODO Recode using ModelForm
    semester = forms.ModelChoiceField(required=False, label_suffix='', label="Semestre",   empty_label="Aucun", queryset=Semester.objects.all())
    subject  = forms.ModelChoiceField(required=False, label_suffix='', label="Matière",    empty_label="Aucun", queryset=Subject.objects.all())
    teacher  = forms.ModelChoiceField(required=False, label_suffix='', label="Enseignant", empty_label="Aucun", queryset=Teacher.objects.all())

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'author', 'year']
        labels     = {'author': "Nom ou pseudo",                          'year': "Année",                          'content': "Entrez votre message ici..."}
        help_texts = {'author': "C'est pas forcément votre vrai nom ;-)", 'year': "Quand avez vous eu ce module ?"}

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("label_suffix", "") # Removes label suffixes for all fields
        super(AddCommentForm, self).__init__(*args, **kwargs)
