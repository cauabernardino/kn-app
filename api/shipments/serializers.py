from rest_framework import serializers
from shipments.models import Shipment


class ShipmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shipment
        fields = ["id", "created_at", "description", "due_date"]
