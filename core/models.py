from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = [('none', 'None'), ('submitter', 'Submitter'), ('reviewer', 'Reviewer')]