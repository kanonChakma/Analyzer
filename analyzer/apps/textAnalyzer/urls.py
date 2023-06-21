from django.urls import path

from .views import SentimentAnalysisView

app_name = "textAnalyzer"
urlpatterns = [
    path("", SentimentAnalysisView.as_view(), name="sentiment-analysis"),
]
