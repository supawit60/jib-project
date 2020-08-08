from django.test import TestCase

from ..models import Certificate


class TestWorker(TestCase):
    def setup(self):
        pass

    def tearDown(self):
        return super().tearDown()

    def test_certificate_should_have_defind_fields(self):
        # Given
        name = 'Django Certificate By ODDS'
        issue_by = 'Proof'

        # When
        certificate = Certificate.objects.create(
            name=name,
            issue_by=issue_by,
        )

        # Then
        assert certificate.name == name
        assert certificate.issue_by == issue_by
