from django.http import HttpResponse
from django.views import View


class Covid19ReportView(View):
    def get(self, request):
        return HttpResponse()
