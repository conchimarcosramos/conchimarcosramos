from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonaViewSet, GastoViewSet, GrupoViewSet, DivisionGastos  # ✅ Corrección aquí

# 🔹 Configuración del router
router = DefaultRouter()
router.register(r'personas', PersonaViewSet)
router.register(r'gastos', GastoViewSet)
router.register(r'grupos', GrupoViewSet)

# 🔹 Definición de las rutas
urlpatterns = [
    path('gastos/division/', DivisionGastos.as_view(), name='division-gastos'),
    path('', include(router.urls)),  
]
