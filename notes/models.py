from django.db import models
from django.core.urlresolvers import reverse
from accounts.models import UserProfile

# Create your models here.
class Note(models.Model):
    user = models.ForeignKey(UserProfile, blank=True, null=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True) #not a required field
    join_date = models.DateTimeField(null=True, blank=True) #due datetime is optional
    created = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)
    Achievements = models.CharField(max_length=255,null = True, blank=True)
    #folder is optional
    Sponsor= models.ForeignKey('Sponsor', related_name= "notes", null=True, blank=True)
    Games = models.ManyToManyField('Games', related_name='notes', null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk":self.pk})
        

class Folder(models.Model):
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title
        
class Tag(models.Model):
    title = models.CharField(max_length=255)
    
    
    def __str__(self):
        return self.title
        
class Sponsor(models.Model):
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title
    
class Games(models.Model):
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title