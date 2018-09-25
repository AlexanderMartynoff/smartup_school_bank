from django.db import models


class Сurrency(models.Model):
    denomination = models.IntegerField(unique=True)
    number = models.IntegerField()
