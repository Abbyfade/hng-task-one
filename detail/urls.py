from django.urls import path
from . import views

app_name = "detail"
urlpatterns = [
    path("", views.index, name="detail"),
]