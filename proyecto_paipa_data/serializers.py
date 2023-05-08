from rest_framework import serializers

from .models import Carac

class Carac3Serializer(serializers.HyperlinkedModelSerializer):
    """
    Serializador para consulta animales vacunados
    """
    num_gatos = serializers.IntegerField()
    num_gatos_vacu = serializers.IntegerField()
    num_perros = serializers.IntegerField()
    num_perros_vacu = serializers.IntegerField()
    num_equino = serializers.IntegerField()
    num_equino_vacu = serializers.IntegerField()
    class Meta:
        model = Carac
        fields = ('estrato', 'num_gatos', 'num_gatos_vacu', 'num_perros', 'num_perros_vacu', 'num_equino', 'num_equino_vacu')

class Carac2Serializer(serializers.HyperlinkedModelSerializer): 
    """
    Serializador para consulta animales por estratos
    """
    num_gatos = serializers.IntegerField()
    num_perros = serializers.IntegerField()
    num_equino = serializers.IntegerField()
    num_aves = serializers.IntegerField()
    num_porcinos = serializers.IntegerField()
    class Meta:
        model = Carac
        fields = ('estrato', 'num_gatos', 'num_perros', 'num_equino', 'num_aves', 'num_porcinos')

class CaracSerializer(serializers.HyperlinkedModelSerializer): 
    """
    Serializador para consulta de cantidad de estratos por areas
    """
    num_estrato = serializers.IntegerField()
    class Meta:
        model = Carac
        fields = ('areas', 'estrato', 'num_estrato')