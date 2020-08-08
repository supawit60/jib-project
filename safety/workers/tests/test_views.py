from django.test import TestCase

from ..models import Worker

import json

from rest_framework.test import APITestCase


class TestWorkerListView(APITestCase):
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
            primary_phone='0888888888',
            secondary_phone='0999999999',
            address='Bangkok',
        )
        Worker.objects.create(
            first_name='Test',
            last_name='Klinhom',
            is_available=False,
            primary_phone='0888888888',
            secondary_phone='0999999999',
            address='Bangkok',
        )

        # When
        response = self.client.get('/workers/')

        # print(response.data)

        # Then
        # self.assertContains(response, '<li>Supawit</li>')
        # self.assertContains(response, '<li>Test</li>')

        # self.maxDiff = None

        excepted = [
            {
                "first_name": "Supawit",
                "last_name": "Klinhom",
                "is_available": True,
                "primary_phone": "0888888888",
                "secondary_phone": "0999999999",
                "address": "Bangkok"
            },
            {
                "first_name": "Test",
                "last_name": "Klinhom",
                "is_available": False,
                "primary_phone": "0888888888",
                "secondary_phone": "0999999999",
                "address": "Bangkok"
            },
        ]

        self.assertEqual(
            response.data,
            excepted
        )
