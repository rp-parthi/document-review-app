# URL Structure — Document Review App

## URL Map

| URL | View | Method | Action |
|---|---|---|---|
| `/register` | `register_view` | GET | Show registration form |
| `/register` | `register_view` | POST | Create user → redirect to `/login` |
| `/login` | `login_view` | GET | Show login form |
| `/login` | `login_view` | POST | Validate credentials → redirect by role |
| `/logout` | `logout_view` | POST | Clear session → redirect to `/login` |
| `/dashboard/submitter` | `submitter_dashboard` | GET | Show submitter's document list |
| `/dashboard/reviewer` | `reviewer_dashboard` | GET | Show reviewer's document list |
| `/documents/upload` | `upload_document` | GET | Show upload form |
| `/documents/upload` | `upload_document` | POST | Save document → redirect to `/dashboard/submitter` |
| `/documents/<id>` | `document_detail` | GET | Show document, comments, and actions |
| `/documents/<id>/edit` | `edit_document` | GET | Show pre-filled edit form |
| `/documents/<id>/edit` | `edit_document` | POST | Save changes → redirect to `/documents/<id>` |
| `/documents/<id>/comment` | `add_comment` | POST | Save comment → redirect to `/documents/<id>` |
| `/documents/<id>/approve` | `approve_document` | POST | Set status Approved → redirect to `/dashboard/reviewer` |
| `/documents/<id>/reject` | `reject_document` | POST | Set status Rejected → redirect to `/dashboard/reviewer` |

---

## Views List

```
register_view
login_view
logout_view
submitter_dashboard
reviewer_dashboard
upload_document
document_detail
edit_document
add_comment
approve_document
reject_document
```

Total: 11 views

---

## Notes

- GET requests show a page
- POST requests process a form submission
- All dashboard and document views require login
- Submitter dashboard only accessible by submitters
- Reviewer dashboard only accessible by reviewers
- Edit page only accessible if document status is Draft
- Approve/Reject only available if document status is Under Review