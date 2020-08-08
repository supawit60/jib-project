from django.contrib import admin
from django.test import TestCase

from ..models import Certificate
from ..admin import CertificateAdmin


class CertifacateAdminTest(TestCase):
    def test_admin_should_be_registered(self):
        assert(isinstance(admin.site._registry[Certificate], CertificateAdmin)) is True

    def test_admin_should_set_list_display(self):
        excepted = (
            'name',
            'issue_by',
        )
        assert CertificateAdmin.list_display == excepted
