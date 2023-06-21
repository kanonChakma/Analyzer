from django.urls import include, path

from .views import SignupView

app_name = "users"

urlpatterns = [
    path("register/", SignupView.as_view(), name="create_user"),
]
