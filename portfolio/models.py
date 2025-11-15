from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    bio = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    stackoverflow_url = models.URLField(blank=True)
    medium_url = models.URLField(blank=True)
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    profile_image_url = models.URLField(blank=True, help_text="External image URL (e.g., from Google Photos, Imgur, etc.)")
    resume_file = models.FileField(upload_to='resume/', blank=True, null=True)
    available_for_hire = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profile'


class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    order = models.IntegerField(default=0)
    icon = models.CharField(max_length=50, blank=True, help_text="Font Awesome icon class")
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['order', 'name']
        verbose_name_plural = 'Skill Categories'


class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills', null=True, blank=True)
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(default=50, help_text="0-100")
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['order', 'name']


class Experience(models.Model):
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True, help_text="Leave blank if current")
    description = models.TextField()
    technologies = models.CharField(max_length=500, blank=True, help_text="Comma-separated")
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.position} at {self.company}"
    
    @property
    def is_current(self):
        return self.end_date is None
    
    def get_technologies_list(self):
        """Return technologies as a list"""
        if self.technologies:
            return [tech.strip() for tech in self.technologies.split(',')]
        return []
    
    class Meta:
        ordering = ['-start_date']
        verbose_name_plural = 'Experience'


class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    grade = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.degree} in {self.field_of_study}"
    
    class Meta:
        ordering = ['-start_date']
        verbose_name_plural = 'Education'


class Project(models.Model):
    STAGE_CHOICES = [
        (0, 'Stage 0'),
        (1, 'Stage 1'),
        (2, 'Stage 2'),
        (3, 'Stage 3'),
    ]
    
    title = models.CharField(max_length=200)
    stage = models.IntegerField(choices=STAGE_CHOICES, default=0)
    description = models.TextField()
    problem_statement = models.TextField(blank=True, help_text="The problem this project solves")
    solution_approach = models.TextField(blank=True, help_text="How the solution addresses the problem")
    technical_architecture = models.TextField(blank=True, help_text="System architecture and component interaction")
    design_decisions = models.TextField(blank=True, help_text="Key technical decisions and trade-offs")
    testing_strategy = models.TextField(blank=True, help_text="Testing approach and coverage")
    api_documentation_url = models.URLField(blank=True, help_text="Swagger/OpenAPI documentation URL")
    project_url = models.URLField(blank=True, help_text="Live project URL")
    github_url = models.URLField(blank=True, help_text="GitHub repository URL")
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    featured = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['order', '-created_at']


class Technology(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='technologies')
    name = models.CharField(max_length=100)
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.project.title} - {self.name}"
    
    class Meta:
        ordering = ['order']
        verbose_name_plural = 'Technologies'


class Testimonial(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    company = models.CharField(max_length=200, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    linkedin_url = models.URLField(blank=True)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.position}"
    
    class Meta:
        ordering = ['order', '-created_at']


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    excerpt = models.TextField(max_length=300)
    content = models.TextField()
    featured_image = models.ImageField(upload_to='blog/', blank=True, null=True)
    tags = models.CharField(max_length=300, blank=True, help_text="Comma-separated")
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']


class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
    
    class Meta:
        ordering = ['-created_at']
