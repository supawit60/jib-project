from django.test import TestCase

from ..models import Certificate
from ..serializers import CertificateModelSerializer


class TestCertificateModelSSerializer(TestCase):
    def test_model_serializer_should_set_certificate_model(self):
        print(dir(CertificateModelSerializer.Meta.model))
        assert CertificateModelSerializer.Meta.model == Certificate

    def test_model_serializer_should_use_all_fiel(self):
        assert CertificateModelSerializer.Meta.fields == '__all__'
