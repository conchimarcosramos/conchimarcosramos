from django.urls import path
from .views import PersonaList, PersonaDetail, GastoList, DividirGastos

urlpatterns = [
    path('personas/', PersonaList.as_view(), name='persona-list'),
    path('persona/<int:pk>/', PersonaDetail.as_view(), name='persona-detail'),  
    path('gastos/', GastoList.as_view(), name='gasto-list'),
    path('dividir/', DividirGastos.as_view(), name='dividir-gastos'),
]
