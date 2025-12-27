from django.core.management.base import BaseCommand
from portfolio.models import Experience
from datetime import date


class Command(BaseCommand):
    help = 'Populate database with experience data'

    def handle(self, *args, **kwargs):
        # Clear existing experiences
        Experience.objects.all().delete()
        self.stdout.write(self.style.WARNING('Cleared existing experiences'))
        
        experiences_data = [
            {
                'position': 'Freelance Backend Developer',
                'company': 'Self-Employed',
                'description': 'Developing custom REST APIs and backend solutions for clients. Focus on Python/Django/FastAPI applications with PostgreSQL databases. Implementing authentication systems, payment integrations (Stripe), background task processing with Celery, and containerized deployments using Docker. Delivering scalable, well-documented APIs with comprehensive testing and CI/CD pipelines.',
                'tech_used': 'Python Django FastAPI PostgreSQL Redis Docker Celery Stripe Git',
                'start_date': date(2024, 1, 1),
                'current': True,
            },
            {
                'position': 'Open Source Contributor',
                'company': 'Various Projects',
                'description': 'Contributing to open-source Python projects, focusing on backend development, API improvements, and documentation. Active participant in code reviews, issue resolution, and community discussions. Building real-world experience through collaborative development practices.',
                'tech_used': 'Python Django FastAPI Git GitHub PostgreSQL',
                'start_date': date(2023, 6, 1),
                'current': True,
            },
        ]

        for exp_data in experiences_data:
            Experience.objects.create(**exp_data)
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created experience: {exp_data["position"]}')
            )

        self.stdout.write(self.style.SUCCESS('Experience population completed!'))
