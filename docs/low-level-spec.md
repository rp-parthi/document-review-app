# Low Level Spec — Document Review App

## Pages and Actions

---

### 1. Register Page

**URL:** `/register`

| Element | Detail |
|---|---|
| Username | Text input |
| Password | Password input |
| Confirm Password | Password input |
| Register button | Creates account → redirects to `/login` |

---

### 2. Login Page

**URL:** `/login`

| Element | Detail |
|---|---|
| Username | Text input |
| Password | Password input |
| Login button | Validates credentials → checks role |

**After login:**
- Role is `submitter` → redirect to `/dashboard/submitter`
- Role is `reviewer` → redirect to `/dashboard/reviewer`
- Role is `none` → show message: *"Your account is pending role assignment. Contact admin."*

---

### 3. Submitter Dashboard

**URL:** `/dashboard/submitter`

| Element | Detail |
|---|---|
| Document list | All documents uploaded by this submitter |
| Per document | Document name, date uploaded, status |
| Upload New Document button | Goes to `/documents/upload` |
| View button (per document) | Goes to `/documents/<id>` |

---

### 4. Reviewer Dashboard

**URL:** `/dashboard/reviewer`

| Element | Detail |
|---|---|
| Document list | All documents assigned to this reviewer |
| Per document | Document name, date uploaded, status |
| View button (per document) | Goes to `/documents/<id>` |

---

### 5. Upload Document Page

**URL:** `/documents/upload`

| Element | Detail |
|---|---|
| Document title | Text input |
| File | File upload (PDF or Word) |
| Assign to Reviewer | Dropdown — list of reviewers |
| Save as Draft button | Saves document → status set to `Draft` → redirects to `/dashboard/submitter` |
| Submit for Review button | Saves document → status set to `Under Review` → redirects to `/dashboard/submitter` |
| Cancel button | Goes back to `/dashboard/submitter` |

---

### 6. Document Detail Page

**URL:** `/documents/<id>`

**Visible to both roles:**

| Element | Detail |
|---|---|
| Document title | Display only |
| Uploaded by | Submitter name |
| Date uploaded | Display only |
| Current status | Draft / Under Review / Approved / Rejected |
| Comments section | List of all comments with author and date |

**Submitter sees:**

| Element | Detail |
|---|---|
| Download button | Downloads the file |
| Edit button | Only visible if status is `Draft` → goes to `/documents/<id>/edit` |
| Comment input | Text box + Post Comment button → posts to `/documents/<id>/comment` |

**Reviewer sees:**

| Element | Detail |
|---|---|
| Download button | Downloads the file |
| Comment input | Text box + Post Comment button → posts to `/documents/<id>/comment` |
| Approve button | Only visible if status is `Under Review` → posts to `/documents/<id>/approve` → redirects to `/dashboard/reviewer` |
| Reject button | Only visible if status is `Under Review` → posts to `/documents/<id>/reject` → redirects to `/dashboard/reviewer` |

---

### 7. Edit Document Page

**URL:** `/documents/<id>/edit`

> Only accessible by the Submitter. Only when document status is `Draft`.

| Element | Detail |
|---|---|
| Document title | Text input — pre-filled |
| File | File upload — option to re-upload |
| Assign to Reviewer | Dropdown — pre-filled |
| Save as Draft button | Saves changes → status stays `Draft` → redirects to `/documents/<id>` |
| Submit for Review button | Saves changes → status set to `Under Review` → redirects to `/dashboard/submitter` |
| Cancel button | Goes back to `/documents/<id>` |

---

## User Management

No custom admin page in v1. Users and roles are managed via Django's built-in admin panel at `/admin`.