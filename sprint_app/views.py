import time

import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .ai_processing import generate_sprint_goals
from .jira_api import fetch_jira_issues


def index(request):
    if request.method == "POST":
        jira_base_url = request.POST.get("jira_base_url")
        jira_email = request.POST.get("jira_email")
        jira_api_token = request.POST.get("jira_api_token")
        board_id = request.POST.get("board_id")
        sprint_name = request.POST.get("sprint_name")

        # Fetch Jira Issues
        issues = fetch_jira_issues(jira_base_url, jira_email, jira_api_token, board_id, sprint_name)

        # Generate AI-powered Sprint Goals
        sprint_goals = generate_sprint_goals(issues)

        return JsonResponse({"issues": issues, "sprint_goals": sprint_goals})

    return render(request, "index.html")


def sprint_result_view(request):
    return render(request, "sprint_result.html")


def fetch_sprint_data(request):
    jira_email = request.GET.get("jira_email", "").strip()
    jira_api_token = request.GET.get("jira_api_token", "").strip()

    # Simulate a loading delay (3-5 seconds)
    time.sleep(3)

    if not jira_email or not jira_api_token:
        # Dummy data when Jira credentials are missing (Test Mode)
        response_data = {
            "test_mode": True,
            "sprint_overview": "This sprint focuses on performance, security, and user experience enhancements.",
            "key_objectives": [
                {"category": "Critical Fixes", "goals": [
                    "Resolve login authentication bug (JIRA-101)",
                    "Fix API rate limiting issues (JIRA-105)"
                ]},
                {"category": "Feature Enhancements", "goals": [
                    "Implement search functionality (JIRA-102)",
                    "Add dark mode toggle (JIRA-104)"
                ]},
                {"category": "Performance Improvements", "goals": [
                    "Optimize database queries (JIRA-103)",
                    "Refactor frontend components (JIRA-106)"
                ]},
            ],
            "risk_analysis": [
                "API rate limiting might delay deployment.",
                "Dependency updates require thorough testing."
            ],
            "bonus_features": [
                "Effort estimation: Medium",
                "Blockers detected: 2 potential issues"
            ]
        }
    else:
        # TODO: Fetch real data from Jira API (Future Implementation)
        response_data = {
            "test_mode": False,
            "message": "Real Jira data will be fetched here."
        }

    return JsonResponse(response_data)


@csrf_exempt
def jira_connect(request):
    """Authenticate with Jira and fetch all boards."""
    jira_email = request.GET.get("jira_email", "").strip()
    api_token = request.GET.get("jira_api_token", "").strip()
    base_url = request.GET.get("jira_base_url", "").strip()

    if not jira_email or not api_token or not base_url:
        return JsonResponse({"status": "error", "message": "Missing credentials"}, status=400)

    # Ensure Jira Base URL starts with 'https://'
    if not base_url.startswith("http://") and not base_url.startswith("https://"):
        base_url = "https://" + base_url

    auth = (jira_email, api_token)
    headers = {"Accept": "application/json"}

    url = f"{base_url}/rest/agile/1.0/board"

    try:
        response = requests.get(url, auth=auth, headers=headers)
        if response.status_code == 401:
            return JsonResponse({"status": "error", "message": "Invalid Jira API token."}, status=401)
        elif response.status_code == 403:
            return JsonResponse({"status": "error", "message": "Access forbidden. Check Jira API permissions."}, status=403)
        elif response.status_code == 200:
            boards = response.json().get("values", [])
            if not boards:
                return JsonResponse({"status": "warning", "message": "No boards found for the given credentials."})
            return JsonResponse({"status": "success", "boards": boards})
        else:
            return JsonResponse({"status": "error", "message": f"Jira API returned HTTP {response.status_code}: {response.text}"}, status=response.status_code)
    except requests.exceptions.RequestException as e:
        return JsonResponse({"status": "error", "message": f"Request failed: {str(e)}"}, status=500)
