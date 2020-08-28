from django.contrib.auth.models import User, Group
from rest_framework import serializers
from pc_shop.models import Prozessor, Bestellung, Bestellung_Produkt

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ProzessorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prozessor
        fields = ['url', 'Artikelnummer', 'Serie', 'Modell', 'Kerne', 'Threads', 'Prozessortakt']
        # 'Codename', 'Turbotakt', 'Sockel', 'TDP'

class BestellungSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bestellung
        fields = ['url', 'Bestellnummer', 'Datum']

class Bestellung_ProduktSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bestellung_Produkt
        fields = ['url', 'Bestellnummer', 'Artikelnummer' , 'Anzahl']