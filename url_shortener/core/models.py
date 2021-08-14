from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UrlData(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    url=models.CharField(max_length=200)
    slug=models.CharField(max_length=15)
    
    def __str__(self):
        return f"{self.user}: Short Url for: {self.url} is {self.slug}"