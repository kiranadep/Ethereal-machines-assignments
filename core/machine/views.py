from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Machine
from .serializers import MachineSerializer
from django.utils import timezone
from datetime import timedelta

# CRUD Operations

class MachineListCreateView(generics.ListCreateAPIView):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer

class MachineDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer

class MachineHistoricalDataView(APIView):
    def get(self, request):
        current_time = timezone.now()
        past_15_minutes = current_time - timedelta(minutes=15)
        
        # Get query params for axis selection (optional)
        axis = request.query_params.get('axis', 'all')  # Can be 'x', 'y', 'z' or 'all'

        if axis == 'x':
            data = Machine.objects.filter(timestamp__gte=past_15_minutes).values('axis_x', 'timestamp')
        elif axis == 'y':
            data = Machine.objects.filter(timestamp__gte=past_15_minutes).values('axis_y', 'timestamp')
        elif axis == 'z':
            data = Machine.objects.filter(timestamp__gte=past_15_minutes).values('axis_z', 'timestamp')
        else:
            data = Machine.objects.filter(timestamp__gte=past_15_minutes)

        # Serialize the data
        serializer = MachineSerializer(data, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
