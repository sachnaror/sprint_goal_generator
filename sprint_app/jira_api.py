import requests


def fetch_jira_issues(jira_base_url, jira_email, jira_api_token, board_id, sprint_name):
    headers = {
        "Authorization": f"Basic {jira_email}:{jira_api_token}",
        "Content-Type": "application/json",
    }

    jira_url = f"{jira_base_url}/rest/agile/1.0/board/{board_id}/sprint"
    response = requests.get(jira_url, headers=headers)

    if response.status_code == 200:
        sprints = response.json().get("values", [])
        sprint_id = next((s["id"] for s in sprints if s["name"] == sprint_name), None)

        if sprint_id:
            issues_url = f"{jira_base_url}/rest/agile/1.0/sprint/{sprint_id}/issue"
            response = requests.get(issues_url, headers=headers)
            if response.status_code == 200:
                return [
                    {"id": i["key"], "title": i["fields"]["summary"], "status": i["fields"]["status"]["name"]}
                    for i in response.json().get("issues", [])
                ]
    return []
