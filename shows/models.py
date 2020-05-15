from django.db import models

# Create your models here.
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



