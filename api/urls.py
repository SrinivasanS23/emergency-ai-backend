from django.urls import path
from api.views import AnalyzeMessageView

urlpatterns = [
    path('analyze/', AnalyzeMessageView.as_view(), name='analyze'),
]
