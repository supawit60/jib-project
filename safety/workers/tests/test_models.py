import os

from django.test import TestCase
from django.core.files import File

from unittest.mock import MagicMock

from ..models import Worker


class TestWorker(TestCase):
    def test_workers_should_have_defind_fields(self):
        # Given
        first_name = 'Keng'
        last_name = 'Mark'
        is_available = True
        primary_phone = '081-689-777x'
        secondary_phone = '081-689-777x'
        address = 'Geeky Base All Star'
        # mock img
        image_mock = MagicMock(spec=File)
        image_mock.name = 'ss.png'

        # When
        worker = Worker.objects.create(
            first_name=first_name,
            last_name=last_name,
            image_profile=image_mock,
            is_available=is_available,
            primary_phone=primary_phone,
            secondary_phone=secondary_phone,
            address=address,
        )

        # Then
        self.assertEqual(worker.first_name, first_name)
        self.assertEqual(worker.last_name, last_name)
        self.assertEqual(worker.image_profile, image_mock.name)
        self.assertEqual(worker.is_available, is_available)
        self.assertEqual(worker.primary_phone, primary_phone)
        self.assertEqual(worker.secondary_phone, secondary_phone)
        self.assertEqual(worker.address, address)

        os.remove('ss.png')
