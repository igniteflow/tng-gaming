from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    battle_net = models.EmailField(blank=True)
    steam = models.CharField(max_length=255, blank=True)
    psn = models.CharField(max_length=255, blank=True)
    
class Computer(models.Model):
    user = models.ForeignKey(User)
    psu = models.CharField(max_length=255, blank=True)
    gpu = models.CharField(max_length=255, blank=True)
    ram = models.CharField(max_length=255, blank=True)
    hdd = models.CharField(max_length=255, blank=True)
    cooling = models.CharField(max_length=255, blank=True)
    mouse = models.CharField(max_length=255, blank=True)
    keyboard = models.CharField(max_length=255, blank=True)
    link = models.URLField(blank=True)
    
    title = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    
    def __unicode__(self):
        return self.title
    
class Monitor(models.Model):
    user = models.ForeignKey(User)
    make = models.CharField(max_length=255, blank=True)
    model = models.CharField(max_length=255, blank=True)
    dimensions = models.CharField(max_length=255, blank=True)
    
    def __unicode__(self):
        return self.model
    
class Console(models.Model):
    user = models.ForeignKey(User)
    make = models.CharField(max_length=255, blank=True)
    model = models.CharField(max_length=255, blank=True)
    
    def __unicode__(self):
        return self.model
    
class Game(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    platform = models.CharField(max_length=255, blank=True)
    
    def __unicode__(self):
        return self.title
    