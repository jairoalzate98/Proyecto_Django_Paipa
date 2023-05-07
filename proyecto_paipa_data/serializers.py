from rest_framework import serializers

from .models import Carac


class CaracSerializer(serializers.HyperlinkedModelSerializer): 
    """
    Serializador para consulta de cantidad de estratos por areas
    """
    num_estrato = serializers.IntegerField()
    class Meta:
        model = Carac
        fields = ('areas', 'estrato', 'num_estrato')