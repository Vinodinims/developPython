Step 1: Initial Understanding of Python such as indentation, coding standards, simple coding.
Step 2: Understanding the capabilities of Python
Step 3: Python Frameworks - Django, Flask

Django:
Built in ORM - Direct connection to the Database
Auth such as User Management and Permissions
Avoids SQL Injection, Forgert and Scripting

Flask:
Lightweight

Fast API:
High Performance WEb Framework
Auto Validation
Serialisation
Asynchronous Programming
Auto Documentation (Open API, JSON Schema)

RAG Pipielins, AI Orchestration Layers, External API Calls Optimisation.
Flask and Django has a Debug Toolbar

Pyramid:
Not a scalable web framework, not much online support

Why Virtual Environment for Python:
Dependency isolation
reproducible environment

Python Main Libraries:
Django for REST Framework to build APIs
PostgreSQL - DB
Celery, RQ for Asynchronous Task Management
Asyncio : Async Programming (Async, Await)
Cache: Redis, Memcache
Django has decorators

"from django.contrib.auth.decorators
import login_required

@login_required
@api_view -> handle only GET requests

djano.test import TestCase"

GIL - Global Interpreter Lock, prevent multiple threads from exec python or use PySpark

Python Generators: yield (lazy evaluations)
no OOM (Out of Memory Error)

ContextManagers: with open ... ensures setup and clean actions

Pickling: Process of serialising python code but this is unsafe so better use JSON

Maintainability : PEP 8

formatters like __init__, __new__

Never do Monkey Patching in coding

__ is called Dunder (Double Underscore)

Built in Loggers - import logging or use Sentry/ Loggly

Realtime Data Handling -> WebSocket Protocol

Django Channels to handle realtime notification and Live Updates.

