from django.urls import path

from .views import jira_connect  # Import the function
from .views import fetch_sprint_data, index, sprint_result_view

urlpatterns = [
    path("", index, name="index"),
    path("fetch_sprint_data/", fetch_sprint_data, name="fetch_sprint_data"),
    path("sprint_result/", sprint_result_view, name="sprint_result"),
    path("jira_connect/", jira_connect, name="jira_connect"),
]


