# Document Review App

A Django web application for submitting and reviewing documents through a structured approval workflow.

## Overview

This app allows users to upload documents for review. Reviewers can read, comment, and make a final approval decision. The project was planned thoroughly before any code was written — specs, ERD, and URL mapping were defined first.

## Core Workflow

```
Upload → Review → Approve / Reject
```

## Tech Stack

- Python 3.12
- Django 6.0
- PostgreSQL
- Deployed on AWS EC2 with Nginx and Gunicorn

## Roles

| Role | Permissions |
|---|---|
| Submitter | Upload documents, save drafts, track status, comment |
| Reviewer | Review assigned documents, comment, approve or reject |

## Planning Documents

All planning was done before writing code. See the `docs/` folder:

- [`docs/high-level-spec.md`](docs/high-level-spec.md) — what the app does, who uses it, what's in scope
- [`docs/low-level-spec.md`](docs/low-level-spec.md) — every page, every button, every action
- [`docs/erd.md`](docs/erd.md) — data model and relationships
- [`docs/url-structure.md`](docs/url-structure.md) — full URL map and views list

## Setup

```bash
# Clone the repo
git clone <your-repo-url>
cd document-review-app

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start server
python manage.py runserver
```

## Status

Currently in development — planning complete, models defined, setup in progress.