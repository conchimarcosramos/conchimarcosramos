# modifico el archivo serializers.py para incluir los modelos Gasto y Grupo, para mejora
# de la API
from rest_framework import serializers
from .models import Gasto, Grupo, Persona

class GastoSerializer(serializers.Serializer):
    """Serializer manual para mayor control"""
    id = serializers.IntegerField(read_only=True)
    descripcion = serializers.CharField(max_length=255)
    importe = serializers.DecimalField(max_digits=10, decimal_places=2)
    fecha = serializers.DateField()
    persona_id = serializers.IntegerField()

    def create(self, validated_data):
        return Gasto.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.descripcion = validated_data.get('descripcion', instance.descripcion)
        instance.importe = validated_data.get('importe', instance.importe)
        instance.fecha = validated_data.get('fecha', instance.fecha)
        instance.persona_id = validated_data.get('persona_id', instance.persona_id)
        instance.save()
        return instance

class PersonaSerializer(serializers.ModelSerializer):
    """Serializer automático para Personas"""
    class Meta:
        model = Persona
        fields = '__all__'

class GrupoSerializer(serializers.ModelSerializer):
    """Serializer automático para Grupos"""
    class Meta:
        model = Grupo
        fields = '__all__'
