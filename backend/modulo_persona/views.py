from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
from .models import Dpi, Persona
from .serializers import PersonaSerializer, DpiSerializer

'''
class DpiListView(APIView):
    def get(self, request, *args, **kwargs):
        dpilista = Dpi.objects.all()

        serializer = Dpi(dpilista, many=True)

        return Response(serializer.data)
    
class DpiDetailView(APIView):
    def get(self, request, *args, **kwargs):
        dpi = get_object_or_404(Persona)
        serializer = DpiSerializer(dpi)

        return Response(serializer.data)



class PersonaListView(APIView):
    def get(self, request, *args, **kwargs):
        personalista = Persona.objects.all()

        serializer = Persona(personalista, many=True)

        return Response(serializer.data)
    
class PersonaDetailView(APIView):
    def get(self, request, *args, **kwargs):
        persona = get_object_or_404(Persona)
        serializer = PersonaSerializer(persona)

        return Response(serializer.data)

'''