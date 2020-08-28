from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from pc_shop.serializers import UserSerializer, GroupSerializer, ProzessorSerializer, BestellungSerializer, Bestellung_ProduktSerializer
from pc_shop.models import Prozessor, Bestellung, Bestellung_Produkt


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProzessorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Prozessor.objects.all()
    serializer_class = ProzessorSerializer
    permission_classes = [permissions.IsAuthenticated]

class BestellungViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Bestellung.objects.all()
    serializer_class = BestellungSerializer
    permission_classes = [permissions.IsAuthenticated]

class Bestellung_ProduktViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Bestellung_Produkt.objects.all()
    serializer_class = Bestellung_ProduktSerializer
    permission_classes = [permissions.IsAuthenticated]