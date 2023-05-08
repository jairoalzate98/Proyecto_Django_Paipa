from django.db.models import Count, Sum, F
from rest_framework import viewsets

from .pagination import CaracPagination
from .serializers import CaracSerializer, Carac2Serializer, Carac3Serializer
from .models import Carac

class AnimalesVacunadosViewSet(viewsets.ModelViewSet):
    serializer_class = Carac3Serializer
    pagination_class = CaracPagination
    
    queryset = Carac.objects.values('estrato').annotate(num_gatos=Sum('gatos_cant'), num_gatos_vacu=Sum('gatos_vacu'), num_perros=Sum('perros_can'), num_perros_vacu=Sum('perros_vac'), num_equino=Sum('equino_can'), num_equino_vacu=Sum('equino_vac')).order_by('estrato')


class AnimalesViewSet(viewsets.ModelViewSet):
    serializer_class = Carac2Serializer
    pagination_class = CaracPagination
    
    queryset = Carac.objects.values('estrato').annotate(num_gatos=Sum('gatos_cant'), num_perros=Sum('perros_can'), num_equino=Sum('equino_can'), num_aves=Sum('aves'), num_porcinos=Sum('porcinos')).order_by('estrato')


class EstratosViewSet(viewsets.ModelViewSet):
    serializer_class = CaracSerializer
    pagination_class = CaracPagination

    queryset = Carac.objects.values('areas', 'estrato').annotate(num_estrato=Count('estrato')).order_by('areas', 'estrato')