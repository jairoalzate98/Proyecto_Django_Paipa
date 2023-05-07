from django.db.models import Count, Sum, F
from rest_framework import viewsets

from .pagination import CaracPagination
from .serializers import CaracSerializer
from .models import Carac


class EstratosViewSet(viewsets.ModelViewSet):
    serializer_class = CaracSerializer
    pagination_class = CaracPagination

    queryset = Carac.objects.values('areas', 'estrato').annotate(num_estrato=Count('estrato')).order_by('areas', 'estrato')