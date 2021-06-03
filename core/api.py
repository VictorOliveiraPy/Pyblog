from core.models import Virtualization, EnvironmentSettings
from core.serializers import VirtualizationSerializer, EnvironmentSettingsSerializer
from rest_framework import viewsets


class VirtualizationView(viewsets.ModelViewSet):
    queryset = Virtualization.objects.all()
    serializer_class = VirtualizationSerializer


class EnvironmentSettingsView(viewsets.ModelViewSet):
    queryset = EnvironmentSettings.objects.all()
    serializer_class = EnvironmentSettingsSerializer
