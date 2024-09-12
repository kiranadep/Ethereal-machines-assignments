from rest_framework import serializers
from .models import Machine

class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = ['id', 'name', 'axis_x', 'axis_y', 'axis_z', 'timestamp']
