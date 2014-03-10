from django.db import models


FAUNA_CHOICES = (
    ('MA', 'Mammal'),
    ('BR', 'Bird'),
    ('RP', 'Reptile')
)


class Animal(models.Model):
    name = models.CharField(max_length=32)
    name_scientific = models.CharField(max_length=32)
    fauna = models.CharField(max_length=2, choices=FAUNA_CHOICES)

    def __unicode__(self):
        return self.name
