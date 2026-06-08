from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = [
        ('none', 'None'), 
        ('submitter', 'Submitter'), 
        ('reviewer', 'Reviewer')
        ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='none')

class Document(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'), 
        ('under_review', 'Under Review'), 
        ('approved', 'Approved'), 
        ('rejected', 'Rejected')
        ]

    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploaded_documents')
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_documents')
    date_uploaded = models.DateField(auto_now_add=True)
    date_reviewed = models.DateField(null=True, blank=True)

class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    comment_date = models.DateField(auto_now_add=True)
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='comments')