from django.db import models

class ActivationCode(models.Model):
    code   = models.TextField(max_lenght=255, blank=false, unique=True)
    rank   = models.PositiveSmallIntegerField(default=0)
    active = models.BooleanField(default=False)
    modif  = models.DateField(auto_now=True)

    def __str__(self):
        return self.code

class Member(models.Model):
    username  = models.TextField(max_lenght=255, unique=True)
    user_rank = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.username
