from django.urls import path

from .views import CertificateModelViewSetView

urlpatterns = [
    path('', CertificateModelViewSetView.as_view()),
]
