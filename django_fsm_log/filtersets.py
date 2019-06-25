from django_filters.rest_framework import FilterSet

from .models import StateLog

class StateLogFilterset(FilterSet):
    class Meta:
        model = StateLog
        fields = {
            'object_id': [
                'exact',
            ],
        }
