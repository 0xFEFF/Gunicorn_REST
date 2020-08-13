from django.db import models

# Create your models here.
class Prozessor(models.Model):
    Serie = models.CharField(max_length=100)
    Modell = models.CharField(max_length=100)
    Codename = models.CharField(max_length=100)
    Kerne = models.FloatField()
    Threads = models.FloatField()
    Prozessortakt = models.FloatField()
    Turbotakt = models.FloatField()
    Sockel = models.CharField(max_length=50)
    TDP = models.CharField(max_length=10)
    