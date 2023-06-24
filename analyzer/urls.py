from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/user/", include("analyzer.apps.accounts.urls", namespace="users")),
    path("api/analyze/", include("analyzer.apps.textAnalyzer.urls", namespace="analyzer")),
    path("api-auth/", include("rest_framework.urls")),
]
