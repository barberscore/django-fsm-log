
# Standard Library
from django_fsm_log.models import StateLog
from rest_framework_json_api.django_filters import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


# Local
from .models import StateLog
from .filtersets import StateLogFilterset
from .serializers import StateLogSerializer



class StateLogViewSet(viewsets.ModelViewSet):
    queryset = StateLog.objects.select_related(
        'content_type',
        'by',
    ).prefetch_related(
    )
    serializer_class = StateLogSerializer
    filterset_class = StateLogFilterset
    filter_backends = [
        DjangoFilterBackend,
    ]
    permission_classes = [
        IsAuthenticated,
    ]
    resource_name = "statelog"
