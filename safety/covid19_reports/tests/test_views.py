from django.test import TestCase
from unittest.mock import patch


class TestCovid19ReportView(TestCase):
    # แก้ปัญหาว่าเวลาไม่มี internet แล้วจะ call api ไม่ได้ ..ได้ไม่เช็ค api จริงๆ
    @patch('covid19_reports.views.requests.get')
    def test_view_should_be_accessible(self, _):
        response = self.client.get('/covid19-reports/')
        self.assertEqual(response.status_code, 200)

    @patch('covid19_reports.views.requests.get')
    def test_view_should_call_covid19_api(self, mock):
        self.client.get('/covid19-reports/')
        mock.assert_called_once_with(
            'https://covid19.th-stat.com/api/open/today')
