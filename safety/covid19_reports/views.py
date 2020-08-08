from django.http import HttpResponse
from django.views import View

import requests


class Covid19ReportView(View):
    def get(self, request):
        requests.get('https://covid19.th-stat.com/api/open/today')
        return HttpResponse()
