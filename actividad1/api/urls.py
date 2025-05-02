from django.urls import path
from .views import PersonaList, PersonaDetail, GastoList, DividirGastos,GastoListCreateView, GastoDetailView,calcular_division_gastos

urlpatterns = [
    path('personas/', PersonaList.as_view(), name='persona-list'),
    path('persona/<int:pk>/', PersonaDetail.as_view(), name='persona-detail'),  
    path('gastos/', GastoList.as_view(), name='gasto-list'),
    path('dividir/', DividirGastos.as_view(), name='dividir-gastos'),
    path('gastos/', GastoListCreateView.as_view(), name='gasto-list'),
    path('gastos/<int:pk>/', GastoDetailView.as_view(), name='gasto-detail'),
    path('gastos/division/', calcular_division_gastos, name='division-gastos'),
]
