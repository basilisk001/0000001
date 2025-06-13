from fasthtml.common import *

app, rt = fast_app(hdrs=(picolink))


@rt("/")
def get():
 from fasthtml.common import *
from sqlite_minutils.db import Database
import uuid

# Initialize FastHTML app with PicoCSS
app, rt = fast_app(pico=True)

# Connect to SQLite database
db = Database("data.db")
services = db.t["services"]
if not services.exists():
    services.create(id=str, name=str, description=str, pk="id")
    # Seed example services
    services.insert({"id": str(uuid.uuid4()), "name": "Consulting", "description": "Expert tech solutions."})
    services.insert({"id": str(uuid.uuid4()), "name": "Development", "description": "Custom web apps."})

# Navbar component
def navbar():
    return Nav(
        Ul(
            Li(A("Home", href="/")),
            Li(A("About", href="/about")),
            Li(A("Services", href="/services")),
            Li(A("Contact", href="/contact")),
            cls="nav-links"
        ),
        cls="container"
    )

# Footer component
def footer():
    return Footer(
        P("© 2025 Project 0000001. All rights reserved."),
        A("X", href="https://x.com", target="_blank"),
        cls="container"
    )

# Home route (Hero section)
@rt("/")
def get():
    return (
        Title("Project 0000001 - Corporate Site"),
        navbar(),
        Main(
            Div(
                H1("Welcome to Project 0000001", cls="fade-in"),
                P("Build the future with cutting-edge tech.", cls="hero-text"),
                Button("Discover More", hx_get="/services", hx_target="#content", cls="cta"),
                cls="hero container"
            ),
            Div(id="content"),
            cls="main-content"
        ),
        footer(),
    )

# About route
@rt("/about")
def get():
    return (
        Title("About Us"),
        navbar(),
        Main(
            Div(
                H1("About Project 0000001"),
                P("We’re a visionary team crafting scalable, modern web solutions. Powered by FastHTML and Vercel, we blend creativity and tech to deliver unparalleled experiences."),
                cls="container"
            ),
            cls="main-content"
        ),
        footer(),
    )

# Services route (Dynamic from SQLite)
@rt("/services")
def get():
    service_list = [Li(H3(s["name"]), P(s["description"])) for s in services.rows]
    return (
        Title("Our Services"),
        navbar(),
        Main(
            Div(
                H1("Our Services"),
                Ul(*service_list, cls="service-list"),
                cls="container"
            ),
            cls="main-content"
        ),
        footer(),
    )

# Contact route (Form with HTMX)
@rt("/contact")
def get():
    return (
        Title("Contact Us"),
        navbar(),
        Main(
            Div(
                H1("Get in Touch"),
                Form(
                    Input(type="text", name="name", placeholder="Your Name", required=True),
                    Input(type="email", name="email", placeholder="Your Email", required=True),
                    Textarea(name="message", placeholder="Your Message", required=True),
                    Button("Send", type="submit", hx_post="/submit", hx_target="#form-result"),
                    Div(id="form-result"),
                    cls="contact-form"
                ),
                cls="container"
            ),
            cls="main-content"
        ),
        footer(),
    )

# Form submission (HTMX)
@rt("/submit")
def post(name: str, email: str, message: str):
    # Simulate saving to DB (extend with sqlite_minutils if needed)
    return P(f"Thanks, {name}! We’ll reply soon.", cls="success")

serve()

serve()
