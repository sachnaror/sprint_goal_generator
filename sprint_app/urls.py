from django.urls import path

from .views import index, save_settings

urlpatterns = [
    path("", index, name="index"),
    path("save-settings/", save_settings, name="save_settings"),
]
