# High Level Spec — Document Review App

## What the App Does

A web application that allows users to submit documents for review. Reviewers can read, comment, and make a final approval decision on each document.

## Core Workflow

```
Upload → Review → Approve / Reject
```

## Document Lifecycle

```
Draft → Under Review → Approved / Rejected
```

## Users

| Role | Description |
|---|---|
| Submitter | Uploads documents and tracks their status |
| Reviewer | Reviews assigned documents and makes decisions |

> User accounts are created via a self-registration page. Roles are assigned by an admin via Django's built-in admin panel.

## Version 1 — In Scope

- User registration and login
- Upload a document and assign it to a reviewer
- Save document as draft or submit for review
- Reviewer can comment on a document
- Reviewer can approve or reject a document
- Submitter can view the decision and comments

## Version 1 — Out of Scope

- Email notifications
- Multiple reviewers per document
- Document version history and re-submission
- Custom admin dashboard