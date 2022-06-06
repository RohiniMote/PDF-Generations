from django.urls import path
from app1.views import PdfView,ReportView


urlpatterns=[
    path('',PdfView),
    path('report/',ReportView)
]