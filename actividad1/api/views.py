from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PersonaSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import GastoSerializer
from django.db.models import Sum
from rest_framework.decorators import api_view
from .models import Gasto, Persona

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

class PersonaDetail(RetrieveUpdateDestroyAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

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
        total_gastos = sum(gasto.importe for gasto in Gasto.objects.all())
        if personas.count() > 0:
            gasto_por_persona = total_gastos / personas.count()
        else:
            gasto_por_persona = 0
        resultado = {
            "total_gastos": total_gastos,
            "gasto_por_persona": gasto_por_persona
        }
        return Response(resultado)

class GastoListCreateView(ListCreateAPIView):
    queryset = Gasto.objects.all()
    serializer_class = GastoSerializer

class GastoDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Gasto.objects.all()
    serializer_class = GastoSerializer



@api_view(['GET'])
def calcular_division_gastos(request):
    personas = Persona.objects.all()
    total_gastos = Gasto.objects.aggregate(total=Sum('importe'))['total'] or 0
    total_personas = personas.count()

    if total_personas == 0:
        return Response({"mensaje": "No hay personas registradas."}, status=400)

    gasto_por_persona = total_gastos / total_personas

    resultado = []
    for persona in personas:
        gastado = Gasto.objects.filter(persona=persona).aggregate(total=Sum('importe'))['total'] or 0
        saldo = gastado - gasto_por_persona
        resultado.append({
            "persona": persona.nombre,
            "gastado": gastado,
            "debe": gasto_por_persona - gastado if saldo < 0 else 0,
            "recibe": saldo if saldo > 0 else 0
        })

    return Response({"total_gastos": total_gastos, "detalles": resultado})
