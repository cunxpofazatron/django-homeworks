from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Sensor
from .serializers import SensorSerializer, MeasurementSerializer


class SensorView(APIView):

    def get(self, request):
        sensors = Sensor.objects.all()
        serializer = SensorSerializer(sensors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SensorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SensorDetailView(APIView):

    def get(self, request, pk):
        sensor = get_object_or_404(Sensor, pk=pk)
        serializer = SensorSerializer(sensor)
        return Response(serializer.data)


class MeasurementView(APIView):

    def post(self, request):
        serializer = MeasurementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
