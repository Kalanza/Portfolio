from django.core.management.base import BaseCommand
from portfolio.models import (Profile, SkillCategory, Skill, Project, Technology,
                             Experience, Education)


class Command(BaseCommand):
    help = 'Populate the database with sample portfolio data'

    def add_arguments(self, parser):
        parser.add_argument(
            '--noinput',
            action='store_true',
            help='Skip confirmation prompts',
        )

    def handle(self, *args, **kwargs):
        # Check if data already exists
        if Profile.objects.exists() and not kwargs.get('noinput'):
            self.stdout.write(self.style.WARNING('Data already exists. Skipping population.'))
            return
        
        # Clear existing data
        Profile.objects.all().delete()
        SkillCategory.objects.all().delete()
        Skill.objects.all().delete()
        Project.objects.all().delete()
        Experience.objects.all().delete()
        Education.objects.all().delete()
        
        # Create Profile
        profile = Profile.objects.create(
            name="Victor Mumo Kalanza",
            title="Backend Developer",
            bio="I am a Junior Backend Developer specializing in creating efficient, scalable, and robust API services. My core technical stack centers around Python and its powerful frameworks, specifically Django and FastAPI. I'm passionate about the entire backend lifecycle, from database design to deployment. I also believe in the power of collaboration and am dedicated to contributing to open-source and making the tech industry more inclusive and accessible.",
            email="kalanzavictor@gmail.com",
            phone="+254 711374284",
            github_url="https://github.com/Kalanza",
            linkedin_url="https://www.linkedin.com/in/victor-kalanza-a10a67261"
        )
        self.stdout.write(self.style.SUCCESS(f'Created profile: {profile.name}'))

        # Create Skill Categories and Skills
        skills_data = {
            'Languages': ['Python', 'JavaScript', 'SQL'],
            'Frameworks': ['Django', 'FastAPI', 'Flask'],
            'Databases': ['PostgreSQL', 'MySQL', 'SQLite', 'Redis'],
            'Tools & Technologies': ['Git', 'GitHub', 'Docker', 'RabbitMQ', 'CI/CD'],
            'APIs & Integration': ['REST APIs', 'HTTPX', 'API Design'],
            'AI & ML': ['LLM Integration', 'RAG', 'AI/NLP'],
        }
        
        for idx, (category_name, skills_list) in enumerate(skills_data.items()):
            category = SkillCategory.objects.create(name=category_name, order=idx)
            for skill_idx, skill_name in enumerate(skills_list):
                Skill.objects.create(
                    category=category,
                    name=skill_name,
                    proficiency=75,  # Default proficiency
                    order=skill_idx
                )
            self.stdout.write(self.style.SUCCESS(f'Created category: {category_name} with {len(skills_list)} skills'))
        
        # Create Experience
        experience_data = [
            {
                'company': 'Freelance',
                'position': 'Backend Developer',
                'location': 'Remote',
                'start_date': '2024-01-01',
                'end_date': None,
                'description': 'Developing scalable APIs and microservices for various clients using Python, Django, and FastAPI. Focus on building robust backend systems with proper testing and documentation.',
                'technologies': 'Python, Django, FastAPI, PostgreSQL, Redis',
                'order': 0
            },
        ]
        
        from datetime import datetime
        for exp_data in experience_data:
            exp_data['start_date'] = datetime.strptime(exp_data['start_date'], '%Y-%m-%d').date()
            if exp_data['end_date']:
                exp_data['end_date'] = datetime.strptime(exp_data['end_date'], '%Y-%m-%d').date()
            Experience.objects.create(**exp_data)
            self.stdout.write(self.style.SUCCESS(f'Created experience: {exp_data["position"]} at {exp_data["company"]}'))
        
        # Create Education
        education_data = [
            {
                'institution': 'Your University',
                'degree': 'Bachelor of Science',
                'field_of_study': 'Computer Science',
                'start_date': '2020-09-01',
                'end_date': '2024-06-01',
                'grade': 'Second Class Upper',
                'description': 'Focused on software engineering, data structures, algorithms, and web development.',
                'order': 0
            },
        ]
        
        for edu_data in education_data:
            edu_data['start_date'] = datetime.strptime(edu_data['start_date'], '%Y-%m-%d').date()
            if edu_data['end_date']:
                edu_data['end_date'] = datetime.strptime(edu_data['end_date'], '%Y-%m-%d').date()
            Education.objects.create(**edu_data)
            self.stdout.write(self.style.SUCCESS(f'Created education: {edu_data["degree"]} from {edu_data["institution"]}'))

        # Create Projects
        projects_data = [
            {
                'title': 'Profile API - Dynamic Endpoint',
                'stage': 0,
                'description': 'A simple RESTful API endpoint that returns user information together with a random cat fact from external API.',
                'problem_statement': 'Developers often need to create quick API endpoints that aggregate data from multiple sources for testing and demonstration purposes. Building such endpoints from scratch can be time-consuming.',
                'solution_approach': 'Created a lightweight FastAPI service that combines static profile data with dynamic content from the Cat Facts API. The endpoint uses HTTPX for efficient async HTTP requests and implements proper error handling for external API failures.',
                'technical_architecture': 'Single FastAPI application with async request handling. Uses HTTPX client for external API calls with timeout and retry logic. Implements response caching to reduce external API calls. Deployed as a serverless function for cost efficiency.',
                'design_decisions': 'Chose FastAPI over Flask for native async support and automatic OpenAPI documentation. HTTPX was selected for its async capabilities and modern API design. Implemented graceful degradation - returns profile data even if external API fails.',
                'testing_strategy': 'Unit tests for endpoint response structure. Integration tests with mocked external API calls. Manual testing with various network conditions to ensure resilience.',
                'api_documentation_url': '',
                'project_url': '',
                'github_url': 'https://github.com/Kalanza/profileapi',
                'technologies': ['Python', 'FastAPI', 'HTTPX', 'REST API']
            },
            {
                'title': 'String Analyzer Service',
                'stage': 1,
                'description': 'A powerful string analysis tool with beautiful web UI. Analyze text for palindromes, character frequency, word count & more.',
                'problem_statement': 'Text analysis is a common requirement in many applications, but implementing comprehensive string analysis features from scratch is repetitive. Users need a centralized tool that provides multiple analysis functions with a clean interface.',
                'solution_approach': 'Built a full-stack application with FastAPI backend providing RESTful endpoints for various text analysis operations. PostgreSQL stores analysis history for logged-in users. Frontend provides real-time analysis with instant visual feedback.',
                'technical_architecture': 'Three-tier architecture: React frontend, FastAPI backend with business logic layer, PostgreSQL database. Backend implements 8+ analysis algorithms (palindrome detection, character frequency, word count, sentiment analysis). Uses connection pooling for database efficiency.',
                'design_decisions': 'PostgreSQL chosen over NoSQL for complex querying of analysis history. Implemented server-side analysis to ensure consistent results across devices. Used SQLAlchemy ORM for database abstraction and easier maintenance. Separated analysis logic into reusable service classes.',
                'testing_strategy': 'Comprehensive unit tests for each analysis algorithm with edge cases. Integration tests for API endpoints. Database tests using pytest fixtures. Frontend component tests with Jest. Achieved 85%+ code coverage.',
                'api_documentation_url': '',
                'project_url': 'https://kalanza-string-analyzer-69c7dd55236f.herokuapp.com/',
                'github_url': 'https://github.com/Kalanza/string-analyzer',
                'technologies': ['Python', 'PostgreSQL', 'FastAPI', 'Heroku', 'Web UI']
            },
            {
                'title': 'Country Currency & Exchange API',
                'stage': 2,
                'description': 'FastAPI service that fetches country data, exchange rates, estimates GDP, and stores results in MySQL with full CRUD APIs.',
                'problem_statement': 'Financial and travel applications need reliable access to country information, currency exchange rates, and economic indicators. Existing APIs are often fragmented, requiring multiple integrations and lacking historical data storage.',
                'solution_approach': 'Aggregator API that fetches data from RestCountries and ExchangeRate-API, performs GDP calculations, and stores results in MySQL. Provides unified CRUD endpoints for cached data with automatic refresh logic. Implements rate limiting to respect external API quotas.',
                'technical_architecture': 'FastAPI backend with async workers for external API calls. MySQL database with normalized schema (countries, currencies, exchange_rates tables). Background Celery tasks for periodic data refresh. Redis cache layer for frequently accessed exchange rates (5-minute TTL).',
                'design_decisions': 'MySQL selected for ACID compliance and complex JOIN operations needed for GDP calculations. Implemented repository pattern for data access abstraction. Used dependency injection for external API clients to facilitate testing. Chose async/await throughout for better concurrency under load.',
                'testing_strategy': 'Unit tests with mocked external APIs using responses library. Integration tests with test database. Load testing with locust to verify 100+ concurrent requests handling. Database migration tests to ensure schema consistency.',
                'api_documentation_url': '',
                'project_url': '',
                'github_url': 'https://github.com/Kalanza/country-exchange-api',
                'technologies': ['FastAPI', 'MySQL', 'HTTPX', 'REST API', 'CRUD']
            },
            {
                'title': 'Telex Task Reminder Agent',
                'stage': 3,
                'description': 'AI-powered task reminder agent integrated with Telex.im to understand natural-language tasks, store them, and send smart reminders.',
                'problem_statement': 'Users want to create task reminders using natural language without rigid syntax requirements. Traditional reminder systems require specific formats and struggle with context understanding, leading to poor user experience.',
                'solution_approach': 'Integrated OpenAI GPT-3.5 for natural language processing to extract task details, dates, and priorities from casual text. Built Telex.im webhook integration for bidirectional messaging. Implemented smart scheduling with timezone awareness and recurring task support.',
                'technical_architecture': 'Event-driven architecture using webhook triggers. FastAPI server processes incoming messages, uses LLM for intent extraction, stores tasks in PostgreSQL with full-text search. Background worker checks due tasks every minute and sends notifications via Telex API. Implements exponential backoff for failed notifications.',
                'design_decisions': 'Chose GPT-3.5 for cost-effectiveness vs GPT-4 while maintaining good NLP accuracy. PostgreSQL with full-text search instead of separate search engine to reduce complexity. Implemented retry queue with dead-letter queue for notification failures. Used APScheduler for flexible task scheduling.',
                'testing_strategy': 'Unit tests for NLP parsing with diverse input examples. Integration tests with Telex API sandbox. Tested timezone handling across 10+ timezones. Load testing with 1000+ scheduled tasks. Monitored LLM token usage and response times.',
                'api_documentation_url': '',
                'project_url': 'https://task-reminder-agent-hng-c5d935d03667.herokuapp.com/',
                'github_url': 'https://github.com/Kalanza/telex-task-agent',
                'technologies': ['Python', 'AI/NLP', 'Telex.im API', 'Task Management', 'Heroku']
            },
            {
                'title': 'Movie Review API',
                'stage': 2,
                'description': 'A lightweight RESTful API for creating, reading, updating, and deleting movie reviews. Stores title, rating, body, author, and timestamp.',
                'problem_statement': 'Movie enthusiasts and content platforms need a simple, reliable API for managing user-generated movie reviews. Existing solutions are either too complex or lack proper data validation and query capabilities.',
                'solution_approach': 'Built a clean REST API with Django REST Framework providing full CRUD operations. Implemented input validation, pagination, filtering, and sorting. Uses SQLite for simplicity in deployment while maintaining data integrity with proper constraints.',
                'technical_architecture': 'Django REST Framework with ViewSets for standardized endpoints. SQLite database with indexed fields for optimized queries. Implements Django ORM with custom managers for complex filtering. CORS configured for frontend integration. Token-based authentication for write operations.',
                'design_decisions': 'Django REST Framework chosen for its robust serialization and built-in browsable API. SQLite used for zero-configuration deployment on PythonAnywhere. Implemented read-only public access with authenticated writes to prevent spam. Used model serializers with field-level validation.',
                'testing_strategy': 'Django TestCase for model validation. APITestCase for endpoint testing with authentication. Test coverage for all CRUD operations and edge cases. Validated rating constraints (1-10) and required fields. Performance testing with 10k+ reviews.',
                'api_documentation_url': '',
                'project_url': 'https://kalanzaa.pythonanywhere.com/',
                'github_url': 'https://github.com/Kalanza/Movie-Review-API-.git',
                'technologies': ['Python', 'REST API', 'PythonAnywhere', 'CRUD', 'SQLite']
            },
            {
                'title': 'Distributed Notification System',
                'stage': 3,
                'description': 'Event-driven microservices architecture for email and push notifications using message queuing and caching.',
                'problem_statement': 'Modern applications require reliable, scalable notification delivery across multiple channels (email, SMS, push). Synchronous notification sending causes request timeouts and poor user experience. Need for retry logic, delivery tracking, and preference management.',
                'solution_approach': 'Microservices architecture with separate services for email, push notifications, and preference management. RabbitMQ message broker decouples notification requests from delivery. Redis caches user preferences and implements rate limiting. PostgreSQL stores delivery logs and analytics.',
                'technical_architecture': 'Four microservices: API Gateway, Email Service, Push Notification Service, Preference Service. RabbitMQ with topic exchanges for message routing. Redis for distributed caching and rate limiting (token bucket algorithm). PostgreSQL for persistent storage. Docker Compose for local orchestration.',
                'design_decisions': 'RabbitMQ chosen over Kafka for simpler setup and excellent support for retry patterns. Implemented dead-letter queues for failed notifications. Redis provides sub-millisecond response times for rate limit checks. Used PostgreSQL over NoSQL for complex analytical queries on delivery data. Each service independently deployable.',
                'testing_strategy': 'Unit tests for each microservice with 80%+ coverage. Integration tests using Testcontainers for RabbitMQ and Redis. Contract testing between services. Load testing with 10k+ messages/minute. Chaos engineering tests (service failures, network delays) to verify resilience.',
                'api_documentation_url': '',
                'project_url': '',
                'github_url': 'https://github.com/Kalanza/distributed-notification-system',
                'technologies': ['RabbitMQ', 'Redis', 'PostgreSQL', 'Microservices', 'Event-Driven']
            },
        ]

        for idx, project_data in enumerate(projects_data):
            technologies = project_data.pop('technologies')
            project = Project.objects.create(order=idx, **project_data)
            
            for tech_idx, tech_name in enumerate(technologies):
                Technology.objects.create(
                    project=project,
                    name=tech_name,
                    order=tech_idx
                )
            
            self.stdout.write(self.style.SUCCESS(f'Created project: {project.title}'))

        self.stdout.write(self.style.SUCCESS('Successfully populated database with sample data!'))
