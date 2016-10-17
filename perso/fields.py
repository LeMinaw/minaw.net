#-*- coding: utf-8 -*-

from django.db import models

class YearField(models.PositiveSmallIntegerField):
    description = "Year"
 
    def get_internal_type(self):
        return "YearField"
 
    def formfield(self, **kwargs):
        defaults = {'min_value': 0, 'max_value': 9999}
        defaults.update(kwargs)
        return super(YearField, self).formfield(**defaults)
