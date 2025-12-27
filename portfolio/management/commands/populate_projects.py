from django.core.management.base import BaseCommand
from portfolio.models import Project


class Command(BaseCommand):
    help = 'Populate database with project data'

    def handle(self, *args, **kwargs):
        # Clear existing projects
        Project.objects.all().delete()
        self.stdout.write(self.style.WARNING('Cleared existing projects'))
        
        projects_data = [
            {
                'title': 'Movie Review API',
                'description': 'A simple, lightweight RESTful API for creating, reading, updating, and deleting movie reviews. It\'s designed to be easy to run locally and extend for small projects, demos, or learning purposes.',
                'tech_stack': 'Python, Django, REST Framework, PostgreSQL',
                'github_link': 'https://github.com/Kalanza/Movie-Review-API-',
                'api_documentation': 'https://kalanzaa.pythonanywhere.com/',
                'order': 1,
            },
            {
                'title': 'Country Exchange API',
                'description': 'A FastAPI-based REST API for retrieving country information and exchange rates. This application fetches real-time data from public APIs and provides endpoints to query, filter, and manage country data. FastAPI service that fetches country data, exchange rates, estimates GDP, and stores results in MySQL with full CRUD APIs.',
                'tech_stack': 'Python, FastAPI, MySQL, REST API',
                'github_link': 'https://github.com/Kalanza/country-exchange-api',
                'order': 2,
            },
            {
                'title': 'Distributed Notification System',
                'description': 'Event-driven microservices architecture for email and push notifications using RabbitMQ, Redis, and PostgreSQL.',
                'tech_stack': 'Python, FastAPI, RabbitMQ, Redis, PostgreSQL, Microservices',
                'github_link': 'https://github.com/Kalanza/distributed-notification-system',
                'order': 3,
            },
            {
                'title': 'E-Commerce Backend API',
                'description': 'A containerized E-commerce REST API with background task processing for email notifications and Stripe integration, fully documented and deployed via CI/CD pipelines.',
                'tech_stack': 'Python, Django, Stripe, Docker, CI/CD, Celery, Redis',
                'github_link': 'https://github.com/Kalanza/E-Commerce-Backend-API-',
                'order': 4,
            },
            {
                'title': 'String Analyzer',
                'description': 'A powerful string analysis tool with beautiful web UI. Analyze text for palindromes, character frequency, word count & more. Built with FastAPI + PostgreSQL. Live demo available!',
                'tech_stack': 'Python, FastAPI, PostgreSQL, HTML, CSS, JavaScript',
                'github_link': 'https://github.com/Kalanza/string-analyzer',
                'order': 5,
            },
        ]

        for project_data in projects_data:
            Project.objects.create(**project_data)
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created project: {project_data["title"]}')
            )

        self.stdout.write(self.style.SUCCESS('Project population completed!'))
