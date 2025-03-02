# Sprint Goal Generator (Django + Jira API + OpenAI)

## 🚀 Features
- AI-powered Sprint Goal Generator using Jira & OpenAI
- Beautiful Bootstrap UI
- PostgreSQL Database
- Docker Support
- CI/CD with GitHub Actions

## 📌 Installation
1. Clone the repository


```
sprint_goal_generator/
│── .env                           # Store Jira & OpenAI credentials
│── .gitignore                     # Ignore unnecessary files
│── README.md                      # Instructions on setup & usage
│── manage.py                       # Django management script
│── requirements.txt                # Dependencies
│── Dockerfile                      # For containerization
│── docker-compose.yml              # Docker setup
│── db.sqlite3 (if using SQLite)
│
├── sprint_app/                     # Main Django app
│   │── __init__.py
│   │── admin.py
│   │── apps.py
│   │── models.py                    # SprintGoal model
│   │── views.py                      # API views
│   │── urls.py                       # URL routing
│   │── forms.py (optional)
│   │── serializers.py                # API serializers for DRF
│   │── services.py                   # Business logic & AI processing
│   │── jira_api.py                   # Handles Jira API communication
│   │── openai_api.py                 # Handles OpenAI API calls
│   │── utils.py                      # Helper functions
│   │── permissions.py                 # API permission settings
│
├── sprint_app/templates/sprint_app/
│   │── index.html                     # Frontend UI
│
├── sprint_app/static/sprint_app/
│   │── styles.css                      # Custom styles
│   │── script.js                        # AJAX handling frontend interactions
│
├── sprint_app/migrations/
│   │── __init__.py
│
├── sprint_project/                     # Django project settings
│   │── __init__.py
│   │── settings.py                      # Project settings
│   │── urls.py
│   │── wsgi.py
│   │── asgi.py
│
└── .github/workflows/ci-cd.yml         # CI/CD setup using GitHub Actions

```
