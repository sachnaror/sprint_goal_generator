from django.db import models


class UserSettings(models.Model):
    jira_email = models.EmailField(primary_key=True)
    jira_base_url = models.URLField(blank=True, null=True)
    jira_api_token = models.CharField(max_length=255, blank=True, null=True)
    board_id = models.CharField(max_length=50, blank=True, null=True)
    sprint_name = models.CharField(max_length=255, blank=True, null=True)
    openai_api_key = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.jira_email
