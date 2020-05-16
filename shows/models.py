from __future__ import unicode_literals
from django.db import models

# Custom modles manager
class ShowManager(models.Manager):
    def basic_validator(self, postData):
        # Any errors will be printed into 
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = "Show title must contain at least 2 characters"
        if len(postData['network']) < 3:
            errors['network'] = "Network name must contian at least 3 characters"
        if len(postData['desc']) > 0 and len(postData['desc']) < 10:
            errors['desc'] = "Description must have at least 10 characters"
        return errors



class Network(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Show(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    network = models.ForeignKey(Network, related_name="shows", on_delete=models.CASCADE)
    release_date = models.DateField(auto_now=False, auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()



