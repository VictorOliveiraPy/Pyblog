from rest_framework import serializers
from core.models import Virtualization, EnvironmentSettings


class VirtualizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Virtualization
        fields = ('id',
                  'title',
                  'contents',
                  )


class EnvironmentSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnvironmentSettings
        fields = ('id',
                  'title',
                  'contents',
                  'import_command'
                  )

