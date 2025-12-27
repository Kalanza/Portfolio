from django.shortcuts import render
from .models import Project, Service, Experience


def home(request):
    """Home page view with hero section"""
    projects = Project.objects.all()[:3]  # Get latest 3 projects for preview
    services = Service.objects.all()
    experiences = Experience.objects.all()[:3]
    
    context = {
        'user': {
            'first_name': 'VICTOR',
            'middle_name': 'MUMO', 
            'last_name': 'KALANZA',
            'role': 'Junior Backend Developer',
            'tagline': 'Building efficient, scalable, and resilient API-driven systems.',
            'bio': """I am a Junior Backend Developer focused on building efficient, scalable, and resilient API-driven systems. My core stack is centered on Python, with hands-on experience using Django and FastAPI to design clean, maintainable backend architectures.

I enjoy working across the entire backend development lifecycle — from database modeling and API design to testing, containerization, and deployment. I place strong emphasis on writing readable, well-structured code and following best practices that support long-term scalability and reliability.

Beyond the technical side, I value collaboration and continuous learning. I actively contribute to open-source projects and believe in using technology as a tool for inclusion, accessibility, and positive impact within the tech ecosystem. I am motivated by environments where ideas are shared openly and systems are built with both users and developers in mind.""",
        },
        'nav_items': [
            'ABOUT ME', 'EXPERIENCE', 'SERVICES', 'PROJECTS', 'CONTACT ME'
        ],
        'projects': projects,
        'services': services,
        'experiences': experiences,
    }
    return render(request, 'portfolio/home.html', context)


def portfolio(request):
    """Portfolio page view with all projects"""
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }
    return render(request, 'portfolio/portfolio.html', context)
