from rest_framework import serializers
from .models import Persona, Gasto

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'

class GastoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gasto
        fields = '__all__'
