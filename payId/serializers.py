from rest_framework import serializers

from .models import LocalPayIdEntity

class LocalPayIdEntitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LocalPayIdEntity
        fields = ('get_uri',)
