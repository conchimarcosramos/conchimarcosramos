from django.urls import path
from .views import PersonaList, PersonaDetail, GastoList, DividirGastos,GastoListCreateView, GastoDetailView,calcular_division_gastos
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GastoViewSet, GrupoViewSet 

urlpatterns = [
    path('personas/', PersonaList.as_view(), name='persona-list'),
    path('persona/<int:pk>/', PersonaDetail.as_view(), name='persona-detail'),  
    path('gastos/', GastoList.as_view(), name='gasto-list'),
    path('dividir/', DividirGastos.as_view(), name='dividir-gastos'),
    path('gastos/', GastoListCreateView.as_view(), name='gasto-list'),
    path('gastos/<int:pk>/', GastoDetailView.as_view(), name='gasto-detail'),
    path('gastos/division/', calcular_division_gastos, name='division-gastos'),
]

router = DefaultRouter()
router.register(r'gastos', GastoViewSet)
router.register(r'grupos', GrupoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]