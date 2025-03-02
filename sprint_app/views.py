import json

from django.http import JsonResponse
from django.shortcuts import redirect, render

from .models import UserSettings


def index(request):
    return render(request, "index.html")

def save_settings(request):
    if request.method == "POST":
        data = json.loads(request.body)
        jira_email = data.get("jira_email")
        if not jira_email:
            return JsonResponse({"error": "Jira Email is required"}, status=400)

        settings, created = UserSettings.objects.get_or_create(jira_email=jira_email)
        settings.jira_base_url = data.get("jira_base_url", settings.jira_base_url)
        settings.jira_api_token = data.get("jira_api_token", settings.jira_api_token)
        settings.board_id = data.get("board_id", settings.board_id)
        settings.sprint_name = data.get("sprint_name", settings.sprint_name)
        settings.openai_api_key = data.get("openai_api_key", settings.openai_api_key)
        settings.save()

        return JsonResponse({"message": "Settings saved successfully!"})

    return JsonResponse({"error": "Invalid request"}, status=400)
