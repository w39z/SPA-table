from django.db import models


class Item(models.Model):
    date = models.DateField('Date')
    name = models.CharField('Name', max_length=100)
    amount = models.IntegerField('Amount')
    distance = models.IntegerField('Distance')

    def __str__(self):
        return self.name
