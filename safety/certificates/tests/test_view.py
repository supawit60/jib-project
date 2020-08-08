from django.test import TestCase

from ..models import Certificate
from ..serializers import CertificateModelSerializer
from ..views import CertificateModelViewSetView


class TestCertificateModelViewSetView(TestCase):
    def test_model_view_set_should_be_queryset(self):
        assert list(CertificateModelViewSetView.queryset) == list(Certificate.objects.all())

    def test_model_view_set_should_be_set_serialzer_class(self):
        assert CertificateModelViewSetView.serializer_class == CertificateModelSerializer
