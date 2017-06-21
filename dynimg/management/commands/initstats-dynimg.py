#-*- coding: utf-8 -*-

from django.core.management.base import BaseCommand, CommandError
from dynimg.models import *
from datetime import timedelta

class Command(BaseCommand):
    help = "Initialises or reinitialises statistics in the DB."
    def handle(self, *args, **options):
        confirm = input("Type 'confirm' to initialise statistics. Warning : It can not be undone ! ")
        if confirm == "confirm":
            try:
                stats = Stat.objects.get(id=1)
            except Stat.DoesNotExist:
                self.stdout.write("No DB entry with id=1, creating one.")
                stats = Stat(id=1)
            stats.displayedImgs  = 0
            stats.registeredImgs = 0
            stats.registeredUrls = 0
            stats.processingTime = timedelta(0)
            stats.save()
            self.stdout.write("Statistics initialised.")
        else:
            raise CommandError("Cancelled.")
