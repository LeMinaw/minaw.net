#-*- coding: utf-8 -*-

from django.db import models

class Stats(models.Model):
    generatedSequences = models.IntegerField (verbose_name="Total des séquences générées" )
    generatedPages     = models.IntegerField (verbose_name="Total des pages générées"     )
    generationTime     = models.DurationField(verbose_name="Total des temps de génération")

    def __str__(self):
        """ For object identification """
        return "STATISTICS" # Stats is a special DB, all stats stored in first object (id=1)

class Word(models.Model):
    word  = models.CharField   (verbose_name="Mot",                  max_length=32)
    likes = models.IntegerField(verbose_name="Nombre de likes"                    )
    date  = models.DateField   (verbose_name="Date du dernier like", auto_now=True)

    def __str__(self):
        """ For object identification """
        return self.word
