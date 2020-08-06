from django.contrib import admin
from django.test import TestCase

from ..models import Worker
from ..admin import WorkerAdmin


class WorkerAdminTest(TestCase):
    def test_admin_should_be_registered(self):
        self.assertTrue(isinstance(admin.site._registry[Worker], WorkerAdmin))

    def test_admin_should_set_list_display(self):
        excepted = (
            'first_name',
            'last_name',
            'is_available',
            'primary_phone',
            'secondary_phone',
            'address',
        )
        self.assertEqual(WorkerAdmin.list_display, excepted)

    def test_admin_should_set_list_filter(self):
        excepted = (
            'is_available',
        )
        self.assertEqual(WorkerAdmin.list_filter, excepted)
