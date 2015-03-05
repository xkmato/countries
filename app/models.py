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


class CountryLanguage(models.Model):
    country = models.ForeignKey(Country, related_name='languages')
    language = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return '%s, %s, %s' % (self.country.id, self.language, self.name)

    @classmethod
    def is_valid(cls, string):
        c = list(cls.objects.filter(name__icontains=string).values_list('country', flat=True).distinct())
        try:
            return Country.is_valid(c[0])
        except Exception as e:
            return None