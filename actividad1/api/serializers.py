# modifico el archivo serializers.py para incluir los modelos Gasto y Grupo, para mejora
# de la API
from rest_framework import serializers
from .models import Gasto, Grupo, Persona

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'

class GastoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gasto
        fields = '__all__'

class GrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupo
        fields = '__all__'
