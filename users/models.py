from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    bio = models.TextField(_('bio'), blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True)
    twitter_handle = models.CharField(max_length=50, blank=True)
    email_verified = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username