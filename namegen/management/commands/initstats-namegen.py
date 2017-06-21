#-*- coding: utf-8 -*-

from django.core.management.base import BaseCommand, CommandError
from namegen.models import *
from datetime import timedelta

class Command(BaseCommand):
    help = "Initialises or reinitialises statistics in the DB."
    def handle(self, *args, **options):
        confirm = input("Type 'confirm' to initialise statistics. Warning : It can not be undone ! ")
        if confirm == "confirm":
            try:
                stats = Stats.objects.get(id=1)
            except Stats.DoesNotExist:
                self.stdout.write("No DB entry with id=1, creating one.")
                stats = Stats(id=1)
            stats.generatedSequences = 0
            stats.generatedPages = 0
            stats.generationTime = timedelta(0)
            stats.save()
            self.stdout.write("Statistics initialised.")
        else:
            raise CommandError("Cancelled.")
