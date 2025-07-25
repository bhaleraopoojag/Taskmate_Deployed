from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class tasklistmodel(models.Model):
    manage_id=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    task=models.CharField(max_length=100)
    done=models.BooleanField(default=False)
    
    class Meta:
        ordering=['id']
    def __str__(self):
        return (self.task) + "-"+  str(self.done) 
    
class contactmodel(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()
    
    def __str__(self):
        return self.name  
    
    