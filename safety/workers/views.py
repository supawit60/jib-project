from rest_framework import viewsets
import json

from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.views import APIView

from .models import Worker


class WorkerSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    is_available = serializers.BooleanField()
    primary_phone = serializers.CharField()
    secondary_phone = serializers.CharField()
    address = serializers.CharField()


class WorkerListView(APIView):
    def get(self, request):
        workers = Worker.objects.all()
        serializer = WorkerSerializer(workers, many=True)
        return Response(serializer.data)


class WorkerModelViewSetView(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
