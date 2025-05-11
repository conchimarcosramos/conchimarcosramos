from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Sum
from .models import Persona, Gasto
from .serializers import GastoSerializer, PersonaSerializer

class GastoViewSet(viewsets.ModelViewSet):
    """Vista optimizada para CRUD de Gastos usando ModelViewSet"""
    queryset = Gasto.objects.all()
    serializer_class = GastoSerializer

class PersonaViewSet(viewsets.ModelViewSet):
    """Vista optimizada para CRUD de Personas"""
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

class DivisionGastos(APIView):
    """Calcula cuánto debe pagar o recibir cada persona y sugiere pagos"""

    def get(self, request):
        personas = Persona.objects.all()
        total_gastos = Gasto.objects.aggregate(total=Sum('importe'))['total'] or 0
        gasto_por_persona = total_gastos / personas.count() if personas.count() > 0 else 0

        resultado = []
        deudores = []
        acreedores = []

        # 🔹 Calcular saldo de cada persona
        for persona in personas:
            gastado = Gasto.objects.filter(persona=persona).aggregate(total=Sum('importe'))['total'] or 0
            saldo = gastado - gasto_por_persona
            resultado.append({
                "persona": persona.nombre,
                "gastado": gastado,
                "debe": max(0, gasto_por_persona - gastado),
                "recibe": max(0, saldo)
            })
            
            if saldo < 0:
                deudores.append({"persona": persona, "deuda": abs(saldo)})
            elif saldo > 0:
                acreedores.append({"persona": persona, "credito": saldo})

        # 🔹 Generar sugerencias de pago
        pagos_sugeridos = []
        while deudores and acreedores:
            deudor = deudores.pop(0)
            acreedor = acreedores.pop(0)
            monto = min(deudor["deuda"], acreedor["credito"])
            pagos_sugeridos.append(f"{deudor['persona'].nombre} debe pagar {monto:.2f}€ a {acreedor['persona'].nombre}")

            # Ajustamos cuentas
            deudor["deuda"] -= monto
            acreedor["credito"] -= monto

            # Si aún tienen saldo pendiente, los mantenemos en la lista
            if deudor["deuda"] > 0:
                deudores.insert(0, deudor)
            if acreedor["credito"] > 0:
                acreedores.insert(0, acreedor)

        return Response({
            "total_gastos": total_gastos,
            "detalle": resultado,
            "pagos_sugeridos": pagos_sugeridos
        })