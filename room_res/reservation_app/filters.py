import django_filters

from .models import Room
from .models import Reservation

class RoomFilters(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    seats = django_filters.NumberFilter()

    seats__gt = django_filters.NumberFilter(field_name='seats', lookup_expr='gt')
    seats__lt = django_filters.NumberFilter(field_name='seats', lookup_expr='lt')
    
    class Meta:
        model = Room 
        fields = ("projector",)
