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
            'role': 'Electrical Engineering Student | Backend Developer',
            'tagline': 'I build scalable backend systems at the intersection of Electrical Engineering and Software Development, driven by a mission to solve real-world problems.',
            'bio': """I build scalable backend systems at the intersection of Electrical Engineering and Software Development, driven by a mission to solve real-world problems through reliable, impact-focused technology.

As an Electrical & Electronics Engineering student at Moi University, my foundation is rooted in renewable energy and sustainable systems. I’ve applied this engineering mindset to community impact projects, including the deployment of solar power solutions for underserved educational institutions, reinforcing my belief in technology as a force for good. I currently serve as Vice Chairman of the IEEE Computer Society (Moi University Chapter), where I actively promote innovation, collaboration, and ethical tech.

On the software side, I’m a Backend Developer specializing in Python, with hands-on experience building robust, high-performance API services using Django and FastAPI. My technical strengths span the full backend lifecycle—database design (PostgreSQL), microservices architecture, containerization with Docker, and building systems that are reliable, maintainable, and scalable.

Beyond engineering and code, I’m passionate about leadership and community building. As the GDG Lead at Moi University, I mentor student developers, organize technical events, and encourage open-source contribution and peer learning.""",
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
