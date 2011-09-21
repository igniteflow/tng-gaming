from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    battle_net = models.EmailField(blank=True)
    steam = models.CharField(max_length=255, blank=True)
    psn = models.CharField(max_length=255, blank=True)