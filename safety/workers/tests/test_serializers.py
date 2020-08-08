from django.test import TestCase

from ..models import Worker
from ..serializers import WorkerSerializer


class TestWorkerSerializer(TestCase):
    def test_serializer_should_return_correct_serializered_data(self):
        worker = Worker.objects.create(
            first_name='Supawit',
            last_name='Klinhom',
            is_available=True,
            primary_phone='0888888888',
            secondary_phone='0999999999',
            address='bangkok',
        )
        serializer = WorkerSerializer(worker)

        excepted = {
            'first_name': 'Supawit',
            'last_name': 'Klinhom',
            'is_available': True,
            'primary_phone': '0888888888',
            'secondary_phone': '0999999999',
            'address': 'bangkok',
        }

        assert serializer.data == excepted
