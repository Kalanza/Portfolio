from django.core.management.base import BaseCommand
from portfolio.models import Project, Service, Experience
import datetime

class Command(BaseCommand):
    help = 'Populates the database with Victor Kalanza\'s electrical engineering and backend portfolio data'

    def handle(self, *args, **options):
        # 1. Clear existing database entries
        Project.objects.all().delete()
        Experience.objects.all().delete()
        Service.objects.all().delete()
        self.stdout.write(self.style.WARNING('Cleared existing projects, experiences, and services'))

        # 2. Populate projects
        # Project 1: Solar Project
        p1 = Project.objects.create(
            title="Regina Yego Girls Center Solar Power Project",
            description="I was a proud team member in this transformative humanitarian engineering initiative funded by IEEE Humanitarian Technologies, aimed at bridging the digital divide through renewable energy. Our team successfully installed and handed over a 6kW stand-alone solar power system at the Regina Yego Girls Center in Uasin Gishu County. The system features 6 x 615W solar panels, a 6kW SRNE inverter, a BYD Lithium Battery LVS, and combiner infrastructure to provide consistent electricity for mentorship, ICT, and night-time programs.",
            tech_stack="Solar PV, Load Calculations, Inverter Sizing, Storage, Combiner Box",
            database_schema="Generation: 6 x 615W High-Efficiency Panels\nConversion: 1 x 6kW SRNE Inverter\nStorage: 1 x BYD Lithium Battery LVS\nInfrastructure: PV Cables & Combiners",
            api_documentation="https://www.ieee.org",
            github_link="https://github.com/Kalanza",
            order=1
        )
        self.stdout.write(self.style.SUCCESS(f"Successfully created project: {p1.title}"))

        # Project 2: Movie Review API (Backend side-skill)
        p2 = Project.objects.create(
            title="Movie Review API (Backend Side-Skill)",
            description="A high-performance RESTful API for movie reviews, featuring nested structures, JWT authentication, user ratings, and search query optimization under PostgreSQL.",
            tech_stack="Python, Django, DRF, PostgreSQL, JWT",
            database_schema="Models: User, Movie, Review (One-to-Many, Many-to-Many), PostgreSQL Indexes",
            api_documentation="https://kalanza.pythonanywhere.com",
            github_link="https://github.com/Kalanza/movie-review-api",
            order=2
        )
        self.stdout.write(self.style.SUCCESS(f"Successfully created project: {p2.title}"))

        # Project 3: Distributed Notification System (Backend side-skill)
        p3 = Project.objects.create(
            title="Distributed Notification System (Backend Side-Skill)",
            description="A lightweight event-driven messaging service using FastAPI and Redis queues to broadcast messages asynchronously to system listeners.",
            tech_stack="FastAPI, Redis, Pub/Sub, Docker",
            database_schema="Queues: Redis list structure, Async Pub/Sub backend",
            api_documentation="",
            github_link="https://github.com/Kalanza",
            order=3
        )
        self.stdout.write(self.style.SUCCESS(f"Successfully created project: {p3.title}"))

        # 3. Populate experiences
        # Experience 1: Vice Chairman
        e1 = Experience.objects.create(
            company="IEEE Computer Society (Moi University Chapter)",
            position="Vice Chairman",
            description="Actively promoting technical innovation, software engineering collaboration, and ethical technology usage. Organizing peer workshops, mentorship events, and coordinate activities for the IEEE Moi University chapter.",
            tech_used="Leadership Community-Building Coordinator Workshops",
            start_date=datetime.date(2024, 6, 1),
            current=True
        )
        self.stdout.write(self.style.SUCCESS(f"Successfully created experience: {e1.position} at {e1.company}"))

        # Experience 2: GDG Lead
        e2 = Experience.objects.create(
            company="Google Developer Groups (GDG) Moi University",
            position="GDG Lead",
            description="Mentoring student developers, organizing technical presentations, coding bootcamps, hackathons, and promoting open-source contributions and peer learning inside Moi University.",
            tech_used="Mentorship Technical-Events Peer-Learning Open-Source",
            start_date=datetime.date(2024, 1, 1),
            current=True
        )
        self.stdout.write(self.style.SUCCESS(f"Successfully created experience: {e2.position} at {e2.company}"))

        # Experience 3: Solar Installation Team
        e3 = Experience.objects.create(
            company="IEEE SIGHT Kenya & Good Kenyan Foundation",
            position="Team Member - Regina Yego Solar Project",
            description="Collaborated in a multi-stakeholder humanitarian engineering team in partnership with Modern Power Systems (MPS) to deploy a 6kW stand-alone off-grid solar power system. Installed PV panels, combiners, inverters, and battery bank.",
            tech_used="Solar-PV Load-Calculations System-Sizing Inverters Batteries",
            start_date=datetime.date(2024, 7, 1),
            end_date=datetime.date(2025, 2, 1),
            current=False
        )
        self.stdout.write(self.style.SUCCESS(f"Successfully created experience: {e3.position} at {e3.company}"))

        # 4. Populate services
        s1 = Service.objects.create(
            title="Solar Energy & PV System Design",
            description="System load sizing, panel/inverter calculations, off-grid battery capacity design, and electrical layout schematic drawings.",
            icon="sun",
            order=1
        )
        s2 = Service.objects.create(
            title="Backend Systems & APIs",
            description="Designing robust RESTful web interfaces in Python, Django REST Framework, and FastAPI. Integrating databases and optimization.",
            icon="code",
            order=2
        )
        s3 = Service.objects.create(
            title="Embedded Systems & IoT",
            description="Prototyping microcontroller circuits, grid interfacing, sensor integrations, and writing firmware linked with backend storage.",
            icon="chip",
            order=3
        )
        self.stdout.write(self.style.SUCCESS("Successfully created services!"))
        
        self.stdout.write(self.style.SUCCESS("Database population with Electrical & Backend content completed!"))
