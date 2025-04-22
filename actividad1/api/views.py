from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Persona
from .serializers import PersonaSerializer
from .models import Gasto

class PersonaList(APIView):
    def get(self, request):
        personas = Persona.objects.all()
        serializer = PersonaSerializer(personas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PersonaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class GastoList(APIView):
    def get(self, request):
        gastos = Gasto.objects.all()
        serializer = GastoSerializer(gastos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GastoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DividirGastos(APIView):
    def get(self, request):
        personas = Persona.objects.all()
        total_gastos = sum(gasto.monto for gasto in Gasto.objects.all())
        if personas.count() > 0:
            gasto_por_persona = total_gastos / personas.count()
        else:
            gasto_por_persona = 0
        resultado = {
            "total_gastos": total_gastos,
            "gasto_por_persona": gasto_por_persona
        }
        return Response(resultado)
