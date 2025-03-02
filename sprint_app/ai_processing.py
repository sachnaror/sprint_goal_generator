import os

import openai
from dotenv import load_dotenv

load_dotenv()

def generate_sprint_goals(issues, openai_api_key):
    openai.api_key = openai_api_key

    prompt = "Given these JIRA issues, generate high-level sprint goals:\n"
    for issue in issues:
        prompt += f"- {issue['id']}: {issue['title']} ({issue['status']})\n"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a project manager."},
                  {"role": "user", "content": prompt}]
    )

    return response["choices"][0]["message"]["content"].split("\n")
