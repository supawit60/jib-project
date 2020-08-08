from django.test import TestCase

from ..models import Certificate
from workers.models import Worker


class TestWorker(TestCase):
    def setup(self):
        pass

    def tearDown(self):
        return super().tearDown()

    def test_certificate_should_have_defind_fields(self):
        # Given
        worker = Worker.objects.create(
            first_name='Supawit',
            last_name='Klinhom',
            is_available=True,
            primary_phone='0888888888',
            secondary_phone='0999999999',
            address='Bangkok',
        )

        name = 'Django Certificate By ODDS'
        issue_by = 'Proof'

        # When
        certificate = Certificate.objects.create(
            name=name,
            issue_by=issue_by,
            worker=worker,
        )

        # Then
        assert certificate.name == name
        assert certificate.issue_by == issue_by
        assert certificate.worker.first_name == worker.first_name
