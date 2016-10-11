#-*- coding: utf-8 -*-

from django import forms

class ParamsForm(forms.Form):
    partsNb    = forms.IntegerField(initial=-1,   required=False, label_suffix='', label="Nombre de séquences (-1 pour aléatoire)")
    minPartsNb = forms.IntegerField(initial=2,    required=False, label_suffix='', label="Nombre minimal de séquences (aléatoire uniquement)")
    maxPartsNb = forms.IntegerField(initial=4,    required=False, label_suffix='', label="Nombre maximal de séquences (aléatoire uniquement)")
    paretoDist = forms.BooleanField(initial=True, required=False, label_suffix='', label="Distribution de Pareto (à défaut, linéaire)")
    onlyOnce   = forms.BooleanField(initial=True, required=False, label_suffix='', label="Unicité des séquences")
    addVoyels  = forms.BooleanField(initial=True, required=False, label_suffix='', label="Disséminer des voyelles")
    wordsNb    = forms.IntegerField(initial=9,    required=True,  label_suffix='', label="Nombre de mots")
