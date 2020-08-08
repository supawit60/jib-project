# from rest_framework import viewsets
# import json

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Worker
from .serializers import WorkerSerializer


class WorkerListView(APIView):
    def get(self, request):
        workers = Worker.objects.all()
        serializer = WorkerSerializer(workers, many=True)
        return Response(serializer.data)


# class WorkerModelViewSetView(viewsets.ModelViewSet):
#     queryset = Worker.objects.all()
#     serializer_class = WorkerSerializer
