from django.db import models

# Create your models here.
class Prozessor(models.Model):
    Serie = models.CharField(max_length=100)
    Modell = models.CharField(max_length=100)
    #Codename = models.CharField(max_length=100)
    Kerne = models.IntegerField()
    Threads = models.IntegerField()
    Prozessortakt = models.FloatField()
    #Turbotakt = models.FloatField()
    #Sockel = models.CharField(max_length=50)
    #TDP = models.CharField(max_length=10)

    class Meta:
        ordering = ['Modell']

class Bestellung(models.Model):
    BestellNummer = models.CharField(max_length=100, primary_key=True)
    Prozessor = models.ManyToManyField(Prozessor)
    Anzahl = models.IntegerField()

"""    
class RAM(models.Model):
    Modellname = models.CharField(max_length=100)
    Gesamtkapazität
    Modulanzahl = models.IntegerField()
    Kapazität_Einzelmodule
    Speicherart = models.CharField(max_length=100)
    Speichertyp = models.CharField(max_length=100)
    Bauform = models.CharField(max_length=100)
    Speicherinterface = models.CharField(max_length=100)
    Max_Frequenz
    Lantenz

class Mainboard(models.Model):
    Kompatible_Prozessor = models.CharField(max_length=100)
    Prozessorhersteller = models.CharField(max_length=100)
    Prozessorsockel = models.CharField(max_length=100)
    RAM_Speicher_Max = models.CharField(max_length=50)
    Unterst_Geschw = models.CharField(max_length=100)
    Unterst_RAM  = models.CharField(max_length=100)
    RAM_Typ = models.CharField(max_length=50)
    Speicherkanäle = models.CharField(max_length=50)
    Speichersteckplätze = models.IntegerField()

class Grafikkarte(models.Model):
    Modell = models.CharField(max_length=100)
    Edition = models.CharField(max_length=100)
    Codename = models.CharField(max_length=100)
    Schnittstelle
    Taktfrequenz_GPU
    Boost_Takt
    Grafikspeicher
    Speichertyp  = models.CharField(max_length=100)
    Taktfrequenz_Speicher

class SSD(models.Model):
    Kapazität
    Modellserie = models.CharField(max_length=100)
    Lesegeschw
    Schreibgeschw
    Cache
    Formfaktor = models.CharField(max_length=100)
    Schnittstelle = models.CharField(max_length=100)
    Chiptyp = models.CharField(max_length=100)

class Netzteil(models.Model):
    Modellserie = models.CharField(max_length=100)
    Leistung
    Kuehlung
    Spezifikation
    Effizienz
    Kabelmanagement

class Gehause(models.Model):
    Modellname = models.CharField(max_length=100)
    Typ = models.CharField(max_length=100)
    Farbe
    Formfaktor = models.CharField(max_length=100)
    Laenge
    Breite
    Hoehe
"""