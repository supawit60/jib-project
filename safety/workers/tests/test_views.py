from django.test import TestCase
from ..models import Worker
import json


class TestWorkerListView(TestCase):
    def test_view_should_be_accessible(self):
        response = self.client.get('/workers/')
        # print(dir(response))
        self.assertEqual(response.status_code, 200)

    def test_view_should_render_list_of_worker_names(self):
        # Given
        Worker.objects.create(
            first_name='Supawit',
            last_name='Klinhom',
            is_available=True,
            primary_phone='08888888',
            secondary_phone='09999999',
            address='Bangkok',
        )
        Worker.objects.create(
            first_name='Test',
            last_name='Klinhom',
            is_available=False,
            primary_phone='08888888',
            secondary_phone='09999999',
            address='Thailand',
        )

        # When
        response = self.client.get('/workers/')

        # Then
        # self.assertContains(response, '<li>Supawit</li>')
        # self.assertContains(response, '<li>Test</li>')

        excepted = [
            {
                'name': 'Supawit'
            },
            {
                'name': 'Test'
            },
        ]

        self.assertEqual(
            response.content.decode('utf-8'),
            json.dumps(excepted)
        )
