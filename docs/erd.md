# Entity Relationship Diagram — Document Review App

## Tables

### User
| Field | Type | Notes |
|---|---|---|
| id | Auto | Primary key |
| username | CharField | Unique |
| password | CharField | Handled by Django |
| role | CharField | Choices: none, submitter, reviewer. Default: none |

> Extends Django's built-in `AbstractUser`. Role is assigned by admin after registration.

---

### Document
| Field | Type | Notes |
|---|---|---|
| id | Auto | Primary key |
| title | CharField | Max 255 characters |
| file | FileField | Uploaded to `documents/` folder |
| status | CharField | Choices: draft, under_review, approved, rejected. Default: draft |
| uploaded_by | ForeignKey → User | CASCADE — document deleted if submitter deleted |
| assigned_to | ForeignKey → User | SET_NULL — set empty if reviewer deleted |
| date_uploaded | DateTimeField | Auto set on creation |
| date_reviewed | DateTimeField | Set only when Approved or Rejected. Null until then |

---

### Comment
| Field | Type | Notes |
|---|---|---|
| id | Auto | Primary key |
| text | TextField | No character limit |
| author | ForeignKey → User | CASCADE — comment deleted if user deleted |
| comment_date | DateTimeField | Auto set on creation |
| document | ForeignKey → Document | CASCADE — comment deleted if document deleted |

---

## Relationships

```
User ──────────────< Document (uploaded_by)
User ──────────────< Document (assigned_to)
Document ──────────< Comment
User ──────────────< Comment (author)
```

## Cascade Rules

```
User deleted → Documents deleted → Comments deleted
Reviewer deleted → Document kept, assigned_to set to empty
Document deleted → Comments deleted
```