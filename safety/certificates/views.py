from rest_framework.viewsets import ModelViewSet

from .models import Certificate
from .serializers import CertificateModelSerializer


class CertificateModelViewSetView(ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateModelSerializer
