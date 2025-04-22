from django.urls import path
from .views import PersonaList, GastoList, DividirGastos

urlpatterns = [
    path('personas/', PersonaList.as_view(), name='persona-list'),
    path('gastos/', GastoList.as_view(), name='gasto-list'),
    path('dividir/', DividirGastos.as_view(), name='dividir-gastos'),
]
