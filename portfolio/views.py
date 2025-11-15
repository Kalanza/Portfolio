from django.shortcuts import render, redirect
from django.contrib import messages
from .models import (Profile, SkillCategory, Project, Experience, 
                     Education, Testimonial, BlogPost, ContactMessage)


def index(request):
    """Main portfolio page view"""
    profile = Profile.objects.first()
    skill_categories = SkillCategory.objects.prefetch_related('skills').all()
    projects = Project.objects.filter(featured=True).prefetch_related('technologies')
    experiences = Experience.objects.all()[:3]  # Latest 3
    education = Education.objects.all()
    testimonials = Testimonial.objects.filter(is_active=True)[:3]
    blog_posts = BlogPost.objects.filter(published=True)[:3]
    
    # Handle contact form submission
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        if name and email and subject and message:
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            messages.success(request, 'Thank you for your message! I will get back to you soon.')
            return redirect('portfolio:index')
        else:
            messages.error(request, 'Please fill in all fields.')
    
    context = {
        'profile': profile,
        'skill_categories': skill_categories,
        'projects': projects,
        'experiences': experiences,
        'education': education,
        'testimonials': testimonials,
        'blog_posts': blog_posts,
    }
    
    return render(request, 'portfolio/index.html', context)
