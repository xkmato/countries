from django.db import models

__author__ = 'awesome'


class Country(models.Model):
    id = models.CharField(max_length=2, primary_key=True)
    name = models.CharField(max_length=64)

    @classmethod
    def is_valid(cls, string):
        if cls.objects.filter(id__iexact=string).exists():
            return cls.objects.get(id__iexact=string)
        try:
            return cls.objects.get(name__icontains=string)
        except Exception as e:
            return None
