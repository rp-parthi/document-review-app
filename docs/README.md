# Document Review App

A Django web application for submitting and reviewing documents through a structured approval workflow — built from scratch with a planning-first approach, and deployed to production.

**Live demo:** [https://docreview.parthiban.dev](https://docreview.parthiban.dev)

## Overview

This app allows users to upload documents for review. Reviewers can read, comment, and make a final approval decision. Every part of the project was planned before a single line of code was written — high level spec, low level spec, ERD, and URL mapping were all defined first. See the `docs/` folder for the full planning process.

## Core Workflow

```
Upload → Review → Approve / Reject
```

## Document Lifecycle

```
Draft → Under Review → Approved / Rejected
```

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3.12, Django 6.0 |
| Database | PostgreSQL |
| Server | Gunicorn + Nginx |
| Process management | systemd |
| Hosting | AWS EC2 |
| DNS | AWS Route 53 |
| SSL | Let's Encrypt (Certbot) |
| Frontend | Django Templates + Bootstrap 5 |

## Roles

| Role | Permissions |
|---|---|
| Submitter | Upload documents, save drafts, edit drafts, track status, comment |
| Reviewer | Review assigned documents, comment, approve or reject |

> New users register via a public sign-up form. Roles are assigned by an admin through Django's built-in admin panel — no self-assignment, keeping access controlled.

## Key Features

- Role-based dashboards (separate views for submitters and reviewers)
- Draft saving so in-progress uploads aren't lost
- File upload and download for documents
- Threaded commenting on each document
- Guarded approve/reject actions — only the assigned reviewer can act, and only while a document is under review
- Django's built-in password validation on registration
- Environment-based configuration (`.env`) — no secrets committed to the repo
- HTTPS in production via Let's Encrypt

## Planning Documents

All planning was done before writing code. See the `docs/` folder:

- [`docs/high-level-spec.md`](docs/high-level-spec.md) — what the app does, who uses it, what's in scope
- [`docs/low-level-spec.md`](docs/low-level-spec.md) — every page, every button, every action
- [`docs/erd.md`](docs/erd.md) — data model and relationships
- [`docs/url-structure.md`](docs/url-structure.md) — full URL map and views list

This structure exists to show the planning process, not just the finished code — the goal was to learn how a real project goes from idea to deployed app.

## Local Setup

```bash
# Clone the repo
git clone https://github.com/<your-username>/document-review-app.git
cd document-review-app

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create a .env file with:
# SECRET_KEY=your-secret-key
# DEBUG=True

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start server
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` and you'll be redirected to the login page.

## Deployment

Deployed on an AWS EC2 instance running Ubuntu, using:

```
Nginx (reverse proxy + static/media files)
        ↓
Gunicorn (WSGI server, managed by systemd)
        ↓
Django application
        ↓
PostgreSQL (database)
```

SSL is handled by Certbot/Let's Encrypt, and the subdomain is managed through Route 53.

## Status

Complete and deployed. Core workflow (register → assign role → upload → review → approve/reject) is fully functional end to end.
