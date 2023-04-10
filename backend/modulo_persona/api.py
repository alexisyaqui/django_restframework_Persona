
from rest_framework import viewsets, permissions

from .serializers import *
from .models import *

class DpiViewSet(viewsets.ModelViewSet):
    queryset = Dpi.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DpiSerializer

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PersonaSerializer

